def fuu():
    """
    It doesn't look quite as good with docstrings loaded by sphinx-autoapi:

    :param baz: Some parameter (notice also that this isn't clickable).

    - ✅ Referenced via ``:paramref:`fuu.baz```: :paramref:`fuu.baz`

    - ❌ Referenced via ``:paramref:`.baz```: :paramref:`.baz`

    - ❌ Referenced via ``:paramref:`baz```: :paramref:`baz`

    - ❌ Referenced via default role as ```fuu.baz```: `fuu.baz`

    - ❌ Referenced via default role as ```.baz```: `.baz`

    - ❌ Referenced via default role as ```baz```: `baz`

    """
