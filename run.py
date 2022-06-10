from run_prtpy_algo import app

DEBUG_MODE = False

if __name__ == '__main__':
    import sys
    sys.path.append('../prtpy')
    app.run(debug=DEBUG_MODE)
