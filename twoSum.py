def twoSum(nums,target):
    posicao1 = 0
    posicao2 = 0
    for x in nums:
        valor1=x
        print(x)
        for x in nums:
            valor2=x

            if (valor1 + valor2) == target:
                if posicao1 != posicao2:
                    return [posicao1,posicao2]

            posicao2 = posicao2 + 1
        posicao1 = posicao1 + 1
        posicao2 = 0

resultado = twoSum([3,2,4],6)
print(resultado)

