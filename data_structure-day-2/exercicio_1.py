# tempo máximo que um software permaneceu sem instabilidades.
# 1 - OK
# 0 - Instabilidades

valores_coletados1 = [0, 1, 1, 1, 0, 0, 1, 1]
# resultado = 3

valores_coletados2 = [1, 1, 1, 1, 0, 0, 1, 1]
# resultado = 4

# ----------- Complexity time O(n)------------------------- #


def stable_time(value: list):
    stability_time = 0
    current_stability = 0
    for i in value:
        if i == 1:
            current_stability += 1
        else:
            current_stability = 0
        if current_stability > stability_time:
            stability_time = current_stability
    return stability_time


result = stable_time(valores_coletados2)
print(result)
