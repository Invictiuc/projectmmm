from sympy import symbols, exp, sin

s = symbols('s')

def compute_signal(a0, a1, b0, b1, b2, kp, Tf, kd, A, T, w, signal_choice):
    # Clamp values
    a0 = max(0.1, min(50, a0))
    a1 = max(0.1, min(50, a1))
    b0 = max(0.1, min(50, b0))
    b1 = max(0.1, min(50, b1))
    b2 = max(0.1, min(50, b2))
    kp = max(0.1, min(50, kp))
    Tf = max(0.1, min(50, Tf))
    kd = max(0.1, min(50, kd))
    A = max(0.1, min(50, A))
    T = max(0.1, min(50, T))
    w = max(0.1, min(50, w))

    # Prostokątny
    squaresignal = A * (1 - exp(-s*T)) / s

    # Harmoniczny
    sinsignal = A * w / (s**2 + w**2)

    # Trójkątny
    trianglesignal = (4 * A) / (T * s**2) * (1 - 2*exp(-s*T/2) + exp(-s*T))

    # Sprawdzenie wyniku
    if signal_choice == 'square':
        return f"Sygnał prostokątny: {squaresignal}"
    elif signal_choice == 'sin':
        return f"Sygnał harmoniczny: {sinsignal}"
    elif signal_choice == 'triangle':
        return f"Sygnał trójkątny: {trianglesignal}"
    else:
        return "Invalid signal choice. Please choose square, sin, or triangle."