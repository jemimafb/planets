import glob
import numpy
import matplotlib.pyplot

filenames = glob.glob('data/inflammation*.csv')
filenames = filenames[0:3]

def analyse(filename):
    print(filename)
    detect_problems(filename)
    plot(filename)

def detect_problems(filename):
    data = numpy.loadtxt(fname = filename, delimiter = ',')
   # print(data.shape)
    if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif data.min(axis=0).sum() == 0:
        print('Minima add up to zero!')
    else:
        print('seems OK!')

    print()

def load_data(filename):
    return numpy.loadtxt(fname = filename, delimiter = ',')
def plot(filename):
    data = numpy.loadtxt(fname = filename, delimiter = ',')
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show()

def center(data1, desired):
    return (data1 - data1.mean()) + desired

z = numpy.zeros((2, 2))
print(z)
print(center(z, 3))

data = load_data('data/inflammation-01.csv')

print('original min, mean, max:', data.min(), data.mean(), data.max())

centered = center(data, 0)

print('original min, mean, max:', centered.min(), centered.mean(), centered.max())

print('stdev before and after:', data.std(), centered.std())

print('stdev before and after?:', data.std()==centered.std())


#for f in filenames:
#    analyse(f)
#print(filenames)
