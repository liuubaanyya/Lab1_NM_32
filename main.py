import math

# Функція, для якої шукаємо корінь
def f(x):
    return x**4 - 5.74*x**3 + 8.18*x - 3.48

# Метод релаксації
def relaxation_method():
    a, b = 0, 5
    m1 = max(abs(4*a**3 - 5.74*3*a**2 + 8.18), abs(4*b**3 - 5.74*3*b**2 + 8.18))
    M1 = max(abs(4*a**3 - 5.74*3*a**2 + 8.18), abs(4*b**3 - 5.74*3*b**2 + 8.18))
    tao = 2 / (m1 + M1)
    q = (M1 - m1) / (M1 + m1)
    
    if q >= 1:
        return None, None
    
    x = a
    epsilon = 1e-4
    num_iterations = math.log((epsilon * (1 - q)) / (M1 - m1)) / math.log(q)
    
    for i in range(int(num_iterations)):
        x = x - tao * f(x)
        
    return x, num_iterations

# Метод простої ітерації
def simple_iteration_method():
    # Виберемо функцію фі(x), наприклад, фі(x) = x + 0.01*f(x)
    def phi(x):
        return x + 0.01 * f(x)
    
    # Визначимо константу для умови збіжності
    delta = 0.01  # За припущенням, що phi'(x) < 1 в [0, 5]
    
    x = 0
    epsilon = 1e-4
    num_iterations = math.log(epsilon * (1 - delta) / abs(f(5) - 5.74 * 3 * 5**2 + 8.18)) / math.log(delta)
    
    for i in range(int(num_iterations)):
        x = phi(x)
        
    return x, num_iterations

# Метод Ньютона
def newton_method():
    # Початкове наближення
    x = 1.0
    
    epsilon = 1e-4
    num_iterations = 0
    
    while True:
        num_iterations += 1
        x_new = x - f(x) / (4*x**3 - 5.74*3*x**2 + 8.18)
        if abs(x_new - x) < epsilon:
            return x_new, num_iterations
        x = x_new

# Викликаємо методи
result_relaxation, iterations_relaxation = relaxation_method()
result_simple_iteration, iterations_simple_iteration = simple_iteration_method()
result_newton, iterations_newton = newton_method()

print("Метод релаксації:")
print(f"Результат: {result_relaxation}")
print(f"Кількість ітерацій: {iterations_relaxation}")

print("\nМетод простої ітерації:")
print(f"Результат: {result_simple_iteration}")
print(f"Кількість ітерацій: {iterations_simple_iteration}")

print("\nМетод Ньютона:")
print(f"Результат: {result_newton}")
print(f"Кількість ітерацій: {iterations_newton}")
