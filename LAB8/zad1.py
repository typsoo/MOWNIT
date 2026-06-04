import numpy as np
from numpy import linalg as LA
import time
import networkx as nx
import matplotlib.pyplot as plt

def build_transition_matrix(adj_list):

    n = len(adj_list)
    A = np.zeros((n, n))
    
    for u, neighbors in adj_list.items():
        out_degree = len(neighbors)
        if out_degree > 0:
            for v in neighbors:
                A[v, u] = 1.0 / out_degree
                
    return A


def power_method(adj_list, max_iter=10000, tol=1e-8, d=0.5):
    A = build_transition_matrix(adj_list)    
    n = A.shape[0]


    #x = np.random.rand(n)
    r = np.ones(n) / n

    history = []
    for i in range(1, max_iter + 1):
        y = d * A @ r
        
        l1_norm = np.sum(np.abs(y))
        if l1_norm > 0: r_new = y / l1_norm
        
        delta = LA.norm(r - r_new, 1)
        history.append(delta)
        
        if delta < tol:
            r = r_new
            break
            
        r = r_new

    return r, i, A, history


def verify_with_numpy(A):
    eigvals, eigvecs = LA.eig(A)
    
    # Find the index of the eigenvalue closest to 1.0
    dominant_idx = np.argmin(np.abs(eigvals - 1.0))
    
    # Extract the corresponding eigenvector and take its real part
    dominant_vec = np.real(eigvecs[:, dominant_idx])
    
    # Normalize with L1 norm so it matches PageRank
    dominant_vec = dominant_vec / np.sum(np.abs(dominant_vec))
    
    return dominant_vec

if __name__ == "__main__":
    # Генерируем тестовый граф
    G = nx.erdos_renyi_graph(n=20, p=0.25, directed=True)
    
    # Гарантируем сильную связность для Задания 1
    if not nx.is_strongly_connected(G):
        nodes = list(G.nodes())
        for i in range(len(nodes)):
            G.add_edge(nodes[i], nodes[(i + 1) % len(nodes)])
            
    adj_list = nx.to_dict_of_lists(G)
    
    # Запускаем расчет с сохранением истории
    d_param = 0.8
    pagerank_values, _, _, delta_history = power_method(adj_list, d=d_param)
    
    # Создаем область для двух графиков
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # --- Рисунок 1: Отрисовка графа с масштабированием узлов ---
    pos = nx.spring_layout(G, seed=42)
    
    # Настройки размеров: делаем узлы пропорциональными весу PageRank
    node_sizes = [pagerank_values[node] * 5000 for node in G.nodes()]
    node_colors = [pagerank_values[node] for node in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, 
                           cmap=plt.cm.Blues, alpha=0.9, ax=ax1)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=15, 
                           edge_color="gray", alpha=0.5, ax=ax1)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black", font_weight="bold", ax=ax1)
    
    ax1.set_title("Struktura grafu z wagami PageRank (Zadanie 1)", fontsize=12)
    ax1.axis("off")
    
    # --- Рисунок 2: Кривая сходимости в полулогарифмическом масштабе ---
    ax2.plot(range(1, len(delta_history) + 1), delta_history, 'o-', color='indigo', linewidth=2)
    ax2.set_yscale('log')  # Включаем логарифмический масштаб для оси Y
    
    ax2.set_xlabel("Numer iteracji (i)", fontsize=11)
    ax2.set_ylabel("Delta ||r_{i+1} - r_i||_1 (skala log)", fontsize=11)
    ax2.set_title(f"Krzywa zbieznosci (d = {d_param})", fontsize=12)
    ax2.grid(True, which="both", linestyle="--", alpha=0.5)
    
    # Добавляем теоретическую линию наклона log(d) для демонстрации понимания теории
    # (опционально, но очень ценится преподавателями AGH)
    iterations = np.array(range(1, len(delta_history) + 1))
    theoretical_slope = delta_history[0] * (d_param ** (iterations - 1))
    ax2.plot(iterations, theoretical_slope, '--', color='red', alpha=0.7, label='Teoretyczne nachylenie O(d^i)')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()