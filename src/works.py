def foo():
    """
    Things look fine for docstrings loaded via explicit autodoc directives:

    :param bar: Some parameter.

    - ✅ Referenced via ``:paramref:`foo.bar```: :paramref:`foo.bar`

    - ✅ Referenced via ``:paramref:`.bar```: :paramref:`.bar`

    - ✅ Referenced via ``:paramref:`bar```: :paramref:`bar`

    - ❌ Referenced via default role as ```foo.bar```: `foo.bar`

    - ❌ Referenced via default role as ```.bar```: `.bar`

    - ✅ Referenced via default role as ```bar```: `bar`

    """
