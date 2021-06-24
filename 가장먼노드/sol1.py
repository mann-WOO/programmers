def solution(n, edge):
    # 연결관계를 나타내는 리스트 nodes
    nodes = [[] for _ in range(n + 1)]
    for (node_a, node_b) in edge:
        nodes[node_a].append(node_b)
        nodes[node_b].append(node_a)

    # 방문여부를 1로부터의 거리로 나타내는 리스트 visited
    visited = [0 for _ in range(n + 1)]
    visited[1] = 1
    # bfs를 위한 큐와 큐 포인터
    q = [1]
    q_pointer = 0
    # 큐 포인터가 큐의 길이 내에 있을 때
    while q_pointer < len(q):
        # 현재 노드를 큐 포인터의 노드로 설정
        current_node = q[q_pointer]
        # 현재 노드에 연결된 노드 중 방문하지 않았다면 거리를 기록하고 큐에 삽입
        for node in nodes[current_node]:
            if not visited[node]:
                visited[node] = visited[current_node] + 1
                q.append(node)
        # 큐 포인터를 한칸 뒤로 보내기
        q_pointer += 1
    # 1로부터의 거리 최댓값 구하기
    max_distance = max(visited)
    # 최댓값의 수 세서 반환하기
    answer = visited.count(max_distance)
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))