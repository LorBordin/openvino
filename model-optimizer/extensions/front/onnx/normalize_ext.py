"""
 Copyright (C) 2018-2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
from extensions.ops.normalize import NormalizeOp
from mo.front.extractor import FrontExtractorOp
from mo.front.onnx.extractors.utils import onnx_attr


class NormalizeFrontExtractor(FrontExtractorOp):
    op = 'Normalize'
    enabled = True

    @classmethod
    def extract(cls, node):
        across_spatial = onnx_attr(node, 'across_spatial', 'i', default=0)
        channel_shared = onnx_attr(node, 'channel_shared', 'i', default=0)
        eps = onnx_attr(node, 'eps', 'f', default=0)
        
        attrs = {'across_spatial': bool(across_spatial),
                 'channel_shared': bool(channel_shared),
                 'eps': eps,
                 'layout': 'NCHW'}

        # update the attributes of the node
        NormalizeOp.update_node_stat(node, attrs)
        return cls.enabled
