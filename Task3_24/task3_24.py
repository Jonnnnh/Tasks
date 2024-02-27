def select_candies(input_file_name, output_file_name, money):
    with open(input_file_name, "r", encoding='utf-8') as file:
        lines = file.readlines()

    candies = []
    for line in lines:
        name, price = line.split()
        price = int(price)
        candies.append((name, price))

    candies.sort(key=lambda x: x[1], reverse=True)

    selected_candies = []
    remaining_money = money
    for candy in candies:
        if candy[1] <= remaining_money:
            selected_candies.append(candy[0])
            remaining_money -= candy[1]
            if remaining_money < min(candies, key=lambda x: x[1])[1]:
                break

    with open(output_file_name, 'w') as file:
        file.write("Selected candies:\n")
        for candy in selected_candies:
            file.write(f"{candy}\n")
        file.write(f"Remaining money: {remaining_money}")

input_files = ["input1.txt", "input2.txt", "input3.txt", "input4.txt"]
money = 300

for i, input_file in enumerate(input_files, start=1):
    output_file = f"output{i}.txt"
    select_candies(input_file, output_file, money)
