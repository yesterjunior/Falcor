#pragma once
#include <cuda_runtime.h>

#include <Falcor.h>


namespace FalcorCUDA
{
    // Initializes the CUDA driver API. Returns true if successful, false otherwise.
    bool initCUDA();

    cudaExternalMemory_t importExternalMemory(ref<Falcor::Resource> pResource);
    void* mapExternalMemory(const cudaExternalMemory_t& externalMemory, unsigned long long size);
    
    void* importResourceToDevicePointer(ref<Falcor::Resource> pResource);
    cudaMipmappedArray_t importTextureToMipmappedArray(ref<Falcor::Texture> pTexture, uint32_t cudaUsageFlags);
    cudaSurfaceObject_t mapTextureToSurfaceObject(ref<Falcor::Texture> pTexture, uint32_t cudaUsageFlags);
    };
