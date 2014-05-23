
# coding: utf-8

# In[ ]:

def analyze(filename):
    data = np.loadtxt(fname=filename, delimiter=',')
    plt.figure(figsize=(10.0, 3.0))
    
    plt.subplot(1, 3, 1)
    plt.ylabel('average')
    plt.plot(data.mean(0))

    plt.subplot(1, 3, 2)
    plt.ylabel('max')
    plt.plot(data.max(0))
    
    plt.subplot(1, 3, 3)
    plt.ylabel('min')
    plt.plot(data.min(0))

    plt.tight_layout()
    plt.savefig(filename + ".pdf")


# In[ ]:

if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt
    import sys
    filename = sys.argv[1]
    print filename
    analyze(filename)

