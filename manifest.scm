(use-modules (gnu packages python)
             (gnu packages python-build)
             (guix packages))

(packages->manifest (list python python-pdm-backend))
