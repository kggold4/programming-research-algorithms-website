import os

from run_prtpy_algo import app

if __name__ == '__main__':
    import sys

    sys.path.append('../prtpy')
    app.run(debug=bool(os.getenv("DEBUG_MODE", default=False)))
