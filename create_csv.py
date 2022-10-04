with open('500q_n1.csv', 'w') as f:
    for i in range(1, 357 + 1):
        f.write(f'<img src="n1_q500_q{i:03}.jpg">\t<img src="n1_q500_a{i:03}.jpg">\t{i}\n')
