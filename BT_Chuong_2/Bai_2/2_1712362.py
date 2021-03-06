import math
from sys import argv
script, input = argv
log = print

# log("Hello world!")


# function convert string arr from file to num arr
def convert_str_arr_to_num_arr(str_arr):
    lenght = len(str_arr)
    for i in range(0, lenght):
        str_arr[i] = int(str_arr[i])
    return str_arr


# str_arr_test = ["1 2 3 4", "1 2 3 4", "1 2 3 4"]
# test = str_arr_test[0].split(" ")
# log(test)
# temp = convert_str_arr_to_num_arr(test)
# log(temp)


# func: lay data tu file - chuyen thanh mang
# input: ten file
# output: mang data
def get_data_from_file(file_name):
    # log(file_name)
    fr = open(file_name, 'r')
    lines = fr.readlines()
    # log(lines)

    # remove \n from arr string
    arr_origin = []
    for line in lines:
        line_striped = line.strip()
        format(arr_origin.append(line_striped))
    # log(arr_origin)

    # split str_arr to separate arr string
    length_of_arr_origin = arr_origin.__len__()
    arr_splited = []
    for i in range(0, length_of_arr_origin):
        arr_splited.append(arr_origin[i].split(" "))
    # log(arr_splited)

    # convert to num arr
    result = []
    lenght_of_arr_splited = arr_splited.__len__()
    for i in range(0, lenght_of_arr_splited):
        result.append(convert_str_arr_to_num_arr(arr_splited[i]))
    fr.close()
    return result


# func gcd - tien de euclid
# input: 2 so nguyen a,b
# output: UCLN cua a,b


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# def gcd(a, b):
#     # Everything divides 0
#     if (a == 0 or b == 0):
#         return 0
#     # base case
#     if (a == b):
#         return a
#     # a is greater
#     if (a > b):
#         return gcd(a - b, b)
#     return gcd(a, b - a)


# func kt so ng to
# input: n - so nguyen bat ky
# output: True or False


def is_primes(n):
    if(n < 2):
        return False
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True

# func kt stn cung nhau
# input: 2 so nguyen
# output: True or false


def is_coprimes(a, b):
    # ab_gcd = gcd(a, b)
    if(gcd(a, b) == 1):
        return True
    else:
        return False


# log(is_coprimes(6, 25))

# phi euler handle

# func phi euler
# input: so nguyen n
# ouput: tong so cac so nto cung nhau voi n hoac -1 neu khong ton tai
def phi_euler(n):
    if(n == 0):
        return 0
    ans = n
    i = 2
    while(i*i <= n):
        if(n % i == 0):
            ans -= ans/i
            while(n % i == 0):
                n /= i
        i += 1
    if(n > 1):
        ans -= ans/n
    return int(ans)


# def phi_euler(n):
    # arr_coprimes_with_n = []
    # i = 2
    # ans = n
    # log("n = ", n)
    # while(i*i <= n):
    #     if(n % i == 0):
    #         ans -= ans/i
    #         while(n % i == 0):
    #             n /= i
    #             arr_coprimes_with_n.append(int(n))
    #     i += 1
    # # for i in range(2, i*i <= n):
    # #     # flag = is_coprimes(i, n)
    # #     log(i)
    # #     # if(flag):
    # #     #     arr_coprimes_with_n.append(i)
    # log("ans = ", ans)
    # log("Arra coprimes:", arr_coprimes_with_n)
    # lenght_arr_coprimes = arr_coprimes_with_n.__len__()
    # if(lenght_arr_coprimes >= 1):
    #     return lenght_arr_coprimes
    # else:
    #     return -1


# log("phi euler", end=": ")
# log(phi_euler(10))


# handle total divisor of n - tong cac uoc so xu ly

# func find divisor of n, tim cac uoc cua n
# input: so tu nhien n
# output: mang cac phan tu la uoc cua n
def divisor_of_n(n):
    # if(n != 0):
    #     result = []
    #     for i in range(1, n+1):
    #         if(n % i == 0):
    #             result.append(i)
    #     return result
    # else:
    #     return -1
    result = []
    i = 1
    while (i <= math.sqrt(n)):
        if(n % i == 0):
            if(n/i == i):
                result.append(i)
            else:
                result.append(i)
                result.append(int(n/i))
        i = i+1
    return result


# func tinh tong cac uoc cua n
# input: so tu nhien n
# output: -1 neu dau vao sai, tong
def total_devisor_of_n(n):
    arr_devisor_of_n = divisor_of_n(n)
    if(arr_devisor_of_n == -1):
        return -1
    else:
        total = 0
        for i in arr_devisor_of_n:
            total = i+total
        return total


# log(divisor_of_n(100))
# log(divisor_of_n(4273843837))

# log("Tong cac uoc", end=": ")
# log(total_devisor_of_n(10))


# handle number of divisor - xu ly so cac uoc so

# func tinh so cac uoc so cua n
# input: so tu nhien n
# output: so cac uoc so cua n
def number_of_divisor(n):
    # rs = divisor_of_n(n)
    # if(rs == -1):
    #     return -1
    # else:
    #     length = rs.__len__()
    #     return length
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            # If divisors are equal,
            # count only one
            if (n / i == i):
                count = count + 1
            else:  # Otherwise count both
                count = count + 2
    return count


# log(number_of_divisor(4273843837))
# for i in range(0, 11):
#     log(i, end=": ")
#     log(number_of_divisor(i))


# log(argv[1]) - input txt
data = get_data_from_file(argv[1])
# log(data)

# func processing: handle ket qua truoc khi ghi vao file
# input: data
# output: data after handle


def processing(datas):
    result = []
    for data in datas:
        result.append([phi_euler(data[0]), total_devisor_of_n(
            data[0]), number_of_divisor(data[0])])
    # log(result)
    return result


# processing(data)


# func ghi kech qua vao file
# input: ten file, data ghi vao file
# output: file kech qua, thong bao ghi thanh cong tren console


def write_result_to_file(file_name, datas):
    # log("Hello write file")
    fw = open(file_name, 'w')
    len_data = datas.__len__()
    # log(datas)
    result = processing(datas)

    # log(result)
    drop_down_count = 1
    for rs in result:
        comma_count = 0
        for value in rs:
            if(comma_count == rs.__len__()-1):
                fw.write(str(value))
            else:
                fw.write(str(value)+",")
            comma_count += 1
        if(drop_down_count < len_data):
            fw.write("\n")
        drop_down_count += 1

    # log(drop_down_count)
    # phi_euler(n)
    # total_devisor_of_n(n)
    # number_of_divisor(n)
    # log(len_data)

    # for i in range(0, len_data):
    # n = data[i][0]
    # result_phi_euler = phi_euler(n)
    # result_total_devisor_of_n = total_devisor_of_n(n)
    # result_number_of_divisor = number_of_divisor(n)

    # if(i == len_data-1):
    #     fw.write(str(result_phi_euler)+"," + str(result_total_devisor_of_n) +
    #              "," + str(result_number_of_divisor))
    # else:
    #     fw.write(str(result_phi_euler)+"," + str(result_total_devisor_of_n) +
    #              "," + str(result_number_of_divisor)+"\n")

    fw.close()


write_result_to_file('2_1712362.txt', data)
