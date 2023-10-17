def toto_media(x):
    sumas = 0
    for i in x:
        sumas = sumas + i
    return sumas/len(x)

def toto_mediana(x):
    x = sorted(x)
    if len(x) % 2 == 0:
        return (x[int(len(x)/2)] + x[int((len(x)/2)-1)])/2
    else:
        return x[int((len(x)/2))]

def toto_moda(x):
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

def toto_rango(x):
    return max(x) - min(x)

def toto_var(x):
    sumas = 0
    for i in x:
        sumas = sumas + i
    media = sumas/len(x)
    sumas2 = 0
    for j in x:
        sumas2 = sumas2 + (j - media)**2
    return sumas2/len(x)

def toto_std(x):
    sumas = 0
    for i in x:
        sumas = sumas + i
    media = sumas/len(x)
    sumas2 = 0
    for j in x:
        sumas2 = sumas2 + (j - media)**2
    return np.sqrt(sumas2/len(x))

def toto_percentiles(x,y):
    x = sorted(x)
    return int(y*len(x)/100)

def toto_mad(x):
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
        return (desv[int(len(desv)/2)] + desv[int((len(desv)/2)-1)])/2
    else:
        return desv[int((len(desv)/2))]