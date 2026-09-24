P2. Стресс-тест научного контента
==================================

Формула с номером и ссылкой
---------------------------

Модель метрики задаётся формулой :math:numref:`eq-metric`.

.. math::
   :label: eq-metric

   y_i = \beta_0 + \beta_1 x_i + \varepsilon_i

Таблица и рисунки
-----------------

В полной версии здесь используются ``figure`` с caption, ``list-table`` и
``sphinx-design`` для двухколоночного блока. MyST-NB добавляет исполнение
notebook, а ``sphinxcontrib-bibtex`` формирует ссылки и список литературы из
``references.bib``.

.. image:: ../../../../docs/assets/p2/static-result.png
   :alt: Статический график

Листинг
-------

.. code-block:: python
   :linenos:

   values = [1, 2, 3]
   print(sum(values) / len(values))
