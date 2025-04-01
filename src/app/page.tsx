'use client'
import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'

export default function Home() {
  return (
    <Canvas style={{ height: '100vh', width: '100%' }}>
      {/* Lighting */}
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} intensity={1} />
      
      {/* 3D Cube */}
      <mesh position={[0, 0, 0]} scale={1}>
        <boxGeometry args={[1, 1, 1]} /> {/* Cube with 1x1x1 size */}
        <meshStandardMaterial color="orange" />
      </mesh>

      {/* Camera Controls */}
      <OrbitControls />
    </Canvas>
  )
}
