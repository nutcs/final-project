a = [(1002, 1, 4, 'f'), (1002, 1, 4, 'fs')]
total_list_star = [1,2,3,4,5]
for st in range(len(a)):
    total_list_star.append(a[st][2])

print(f'total_list_star = {sum(total_list_star)}')
print(f'average_star = {sum(total_list_star) / len(total_list_star)}')
print(f'ทั้งหมด {len(total_list_star)} ความคิดเห็น')

star1_list = total_list_star.count(4)

def find_energy(number):
    return total_list_star.count(number) / len(total_list_star) * 100


# width max = 15
print(f'1ดาว = {"%.1f"%(find_energy(1))} %  ; width = {find_energy(2) // 6.6666}')
print(f'1ดาว = {"%.1f"%(find_energy(2))} %  ; width = {find_energy(2) // 6.6666}')
print(f'1ดาว = {"%.1f"%(find_energy(3))} %  ; width = {find_energy(3) // 6.6666}')
print(f'1ดาว = {"%.1f"%(find_energy(4))} %  ; width = {find_energy(4) // 6.6666}')
print(f'1ดาว = {"%.1f"%(find_energy(5))} %  ; width = {find_energy(5) // 6.6666}')
