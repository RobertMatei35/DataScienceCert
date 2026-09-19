# Virtual environments for Module 5 notebooks

The notebooks in this module use pinned package versions. A virtual environment keeps these versions separate from the main Python installation and from other courses.

## 1. Create the environment

Open PowerShell in this folder:

```powershell
cd "D:\LEARNING\CURSURI\DataScience\09_MachineLearningWithPython\Module 5 - Evaluating and Validationg ML Models"
py -m venv .venv-module5
.\.venv-module5\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-module5.txt
python -m ipykernel install --user --name datascience-module5 --display-name "Python (DataScience Module 5)"
```

If PowerShell blocks script activation, use the interpreter directly instead:

```powershell
.\.venv-module5\Scripts\python.exe -m pip install -r requirements-module5.txt
.\.venv-module5\Scripts\python.exe -m ipykernel install --user --name datascience-module5 --display-name "Python (DataScience Module 5)"
```

## 2. Select the environment in VS Code

1. Open a Module 5 notebook.
2. Select the kernel picker in the upper-right corner.
3. Choose **Python (DataScience Module 5)**.
4. Restart the kernel if the notebook was already open.
5. Run the first package-check cell. It should print the `.venv-module5` path and the pinned versions.

The kernel selection is stored by VS Code for the notebook. Repeat the selection for another notebook if VS Code asks for it.

## 3. Run notebooks

After the kernel check succeeds, run the import cell and the remaining cells. The notebooks should not run `pip install` themselves. Install or upgrade packages from PowerShell with the environment selected, then restart the notebook kernel.

To leave the environment in a terminal:

```powershell
deactivate
```

To remove and recreate it later, close notebook kernels first, then run:

```powershell
Remove-Item -Recurse -Force .venv-module5
```

Run the creation steps again after removal.

## Why this works

A notebook imports packages from the Python interpreter attached to its kernel, not necessarily from the Python selected in another terminal. Installing with `python -m pip` after activating the environment guarantees that pip belongs to that interpreter. Installing `ipykernel` registers the environment as a selectable notebook kernel.

Keep one environment per incompatible package set. These three Module 5 notebooks share the package set in `requirements-module5.txt`; notebooks elsewhere in the course can use their own environment and requirements file.

## Troubleshooting

- **Package not found:** confirm the notebook kernel is **Python (DataScience Module 5)**, then run the install command again with `.venv-module5\Scripts\python.exe`.
- **Wrong versions:** restart the kernel after installing or changing packages.
- **Kernel does not appear:** run the `ipykernel install` command again and reload VS Code.
- **Check the active interpreter:** run `import sys; print(sys.executable)` in a notebook cell. It should end with `.venv-module5\Scripts\python.exe`.
