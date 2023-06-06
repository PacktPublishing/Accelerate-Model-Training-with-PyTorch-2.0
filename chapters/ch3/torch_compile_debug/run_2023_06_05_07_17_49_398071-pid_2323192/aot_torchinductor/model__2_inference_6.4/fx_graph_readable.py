class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: f32[32, 1, 3, 3], arg1_1: f32[32], arg2_1: f32[64, 32, 3, 3], arg3_1: f32[64], arg4_1: f32[512, 3136], arg5_1: f32[512], arg6_1: f32[10, 512], arg7_1: f32[10], arg8_1: f32[16, 1, 28, 28]):
        # File: /tmp/ipykernel_2323192/3432332073.py:19, code: out = self.layer1(x)
        convolution: f32[16, 32, 28, 28] = torch.ops.aten.convolution.default(arg8_1, arg0_1, arg1_1, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  arg8_1 = arg0_1 = arg1_1 = None
        relu: f32[16, 32, 28, 28] = torch.ops.aten.relu.default(convolution);  convolution = None
        max_pool2d_with_indices = torch.ops.aten.max_pool2d_with_indices.default(relu, [2, 2], [2, 2]);  relu = None
        getitem: f32[16, 32, 14, 14] = max_pool2d_with_indices[0]
        getitem_1: i64[16, 32, 14, 14] = max_pool2d_with_indices[1];  max_pool2d_with_indices = None
        
        # File: /tmp/ipykernel_2323192/3432332073.py:20, code: out = self.layer2(out)
        convolution_1: f32[16, 64, 14, 14] = torch.ops.aten.convolution.default(getitem, arg2_1, arg3_1, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  getitem = arg2_1 = arg3_1 = None
        relu_1: f32[16, 64, 14, 14] = torch.ops.aten.relu.default(convolution_1);  convolution_1 = None
        max_pool2d_with_indices_1 = torch.ops.aten.max_pool2d_with_indices.default(relu_1, [2, 2], [2, 2]);  relu_1 = None
        getitem_2: f32[16, 64, 7, 7] = max_pool2d_with_indices_1[0]
        getitem_3: i64[16, 64, 7, 7] = max_pool2d_with_indices_1[1];  max_pool2d_with_indices_1 = None
        
        # File: /tmp/ipykernel_2323192/3432332073.py:21, code: out = out.reshape(out.size(0), -1)
        view: f32[16, 3136] = torch.ops.aten.view.default(getitem_2, [16, 3136]);  getitem_2 = None
        
        # File: /tmp/ipykernel_2323192/3432332073.py:22, code: out = self.fc1(out)
        permute: f32[3136, 512] = torch.ops.aten.permute.default(arg4_1, [1, 0]);  arg4_1 = None
        addmm: f32[16, 512] = torch.ops.aten.addmm.default(arg5_1, view, permute);  arg5_1 = view = permute = None
        
        # File: /tmp/ipykernel_2323192/3432332073.py:23, code: out = self.fc2(out)
        permute_1: f32[512, 10] = torch.ops.aten.permute.default(arg6_1, [1, 0]);  arg6_1 = None
        addmm_1: f32[16, 10] = torch.ops.aten.addmm.default(arg7_1, addmm, permute_1);  arg7_1 = addmm = permute_1 = None
        return (addmm_1,)
        