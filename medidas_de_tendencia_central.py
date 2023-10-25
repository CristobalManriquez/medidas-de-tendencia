def toto_media(z):
    """
    Para una lista de números, retorna el valor de la media.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    
    Retorna
    ----------
    media : float
        Valor de la media.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    sumas = 0
    for i in x:
        sumas = sumas + i
    media = sumas/len(x)
    return media

def toto_mediana(z):
    """
    Para una lista de números, retorna el valor de la mediana.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    
    Retorna
    ----------
    mediana : float
        Valor de la mediana.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    x = sorted(x)
    if len(x) % 2 == 0:
        mediana = (x[int(len(x)/2)] + x[int((len(x)/2)-1)])/2
        return mediana
    else:
        mediana = x[int((len(x)/2))]
        return mediana

def toto_moda(z):
    """
    Para una lista de elementos, retorna el valor de la moda.
    
    Parámetros
    ----------
    z : list
        Lista de elementos.
    
    Retorna
    ----------
    moda : list
        Valor de la moda.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    elementos = []
    for i in x:
        if i not in elementos:
            elementos.append(i)
    frecuencia = 0
    moda = []
    for j in elementos:
        if x.count(j) > frecuencia:
            frecuencia = x.count(j)
            moda = [j]
        elif x.count(j) == frecuencia:
            moda.append(j)
    return moda

def toto_rango(z):
    """
    Para una lista de números, retorna el valor del rango.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    
    Retorna
    ----------
    rango : float
        Valor del rango.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    rango = max(x) - min(x)
    return rango

def toto_var(z):
    """
    Para una lista de números, retorna el valor de la varianza.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    
    Retorna
    ----------
    varianza : float
        Valor de la varianza.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    sumas = 0
    for i in x:
        sumas = sumas + i
    media = sumas/len(x)
    sumas2 = 0
    for j in x:
        sumas2 = sumas2 + (j - media)**2
    varianza = sumas2/len(x)
    return varianza

def toto_std(z):
    """
    Para una lista de números, retorna el valor de la desviación estándar.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    
    Retorna
    ----------
    std : float
        Valor de la desviación estándar.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    sumas = 0
    for i in x:
        sumas = sumas + i
    media = sumas/len(x)
    sumas2 = 0
    for j in x:
        sumas2 = sumas2 + (j - media)**2
    std = (sumas2/len(x))**(1/2)
    return std

def toto_mad(z):
    """
    Para una lista de números, retorna el valor de la desviación mediana absoluta.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    
    Retorna
    ----------
    mad : float
        Valor de la desviación mediana absoluta.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    x = sorted(x)
    if len(x) % 2 == 0:
        mediana = (x[int(len(x)/2)] + x[int((len(x)/2)-1)])/2
    else:
        mediana = x[int((len(x)/2))]
    desv = []
    for i in x:
        desv.append(abs(i - mediana))
    desv = sorted(desv)
    if len(desv) % 2 == 0:
        mad = (desv[int(len(desv)/2)] + desv[int((len(desv)/2)-1)])/2
        return mad
    else:
        mad = desv[int((len(desv)/2))]
        return mad

def toto_percentiles(z,y):
    """
    Para una lista de números, retorna el valor del percentil solicitado.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    y : int
        Percentil a retornar.
    
    Retorna
    ----------
    percentil : float
        Valor del percentil solicitado.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    x = sorted(x)
    per = (y/100)*(len(x)-1)
    ponderacion = per - int(per)
    if ponderacion == 0:
        percentil = x[int(per)]
        return percentil
    else:
        percentil = x[int(per)]*(1-ponderacion) + x[int(per)+1]*ponderacion
        return percentil

def toto_cuartiles(z,y):
    """
    Para una lista de números, retorna el valor del cuartil solicitado.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    y : int
        cuartil a retornar.
    
    Retorna
    ----------
    cuartil : float
        Valor del cuartil solicitado.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    x = sorted(x)
    cuar = (y/4)*(len(x)-1)
    ponderacion = cuar - int(cuar)
    if ponderacion == 0:
        cuartil = x[int(cuar)]
        return cuartil
    else:
        cuartil = x[int(cuar)]*(1-ponderacion) + x[int(cuar)+1]*ponderacion
        return cuartil
    
def toto_IQR(z):
    """
    Para una lista de números, retorna el valor del rango intercuartílico.
    
    Parámetros
    ----------
    z : list
        Lista de números.
    
    Retorna
    ----------
    IQR : float
        Valor del rango intercuartílico.
    """
    x = []
    for j in z:
        if j == j:
            x.append(j)
    x = sorted(x)
    Q1 = (1/4)*(len(x)-1)
    P1 = Q1 - int(Q1)
    Q3 = (3/4)*(len(x)-1)
    P3 = Q3 - int(Q3)
    if P1 == 0:
        val_Q1 = x[int(Q1)]
    else:
        val_Q1 = x[int(Q1)]*(1-P1) + x[int(Q1)+1]*P1
    if P3 == 0:
        val_Q3 = x[int(Q3)]
    else:
        val_Q3 = x[int(Q3)]*(1-P3) + x[int(Q3)+1]*P3
    IQR = val_Q3-val_Q1
    return IQR