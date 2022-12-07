"Katherine Rodriguez 22-0018 Refinando código"


def costos_lista():
  with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
  gift_costs = [int(c) for c in gift_costs]

  # convierte strings a int
  return gift_costs


def total(gift_costs):
  gift_costs = costos_lista()
  total_price = 0
  for cost in gift_costs:
    if cost > 1000:
      total_price += cost * 1.16
      # agrega impuestos
    else:
      total_price += cost
      # los costos menores a 1000 no se le agrega impuesto

  return total_price


# llama a los dos funciones y luego imprime el resultado
def main():
  print(total(costos_lista))


if __name__ == '__main__':
  main()