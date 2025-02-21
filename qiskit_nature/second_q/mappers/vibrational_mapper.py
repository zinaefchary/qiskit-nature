# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Vibrational Mapper."""

from __future__ import annotations

from qiskit.opflow.primitive_ops import PauliSumOp

from qiskit_nature.second_q.operators import VibrationalOp

from .qubit_mapper import ListOrDictType, QubitMapper


class VibrationalMapper(QubitMapper):
    """Mapper of Vibrational Operator to Qubit Operator"""

    def map(
        self,
        second_q_ops: VibrationalOp | ListOrDictType[VibrationalOp],
        *,
        register_length: int | None = None,
    ) -> PauliSumOp | ListOrDictType[PauliSumOp]:
        return super().map(second_q_ops, register_length=register_length)
