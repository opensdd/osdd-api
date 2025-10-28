import typescript from '@rollup/plugin-typescript';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { defineConfig } from 'rollup';
import { builtinModules } from 'node:module';

// Base configuration for both browser and Node.js
const baseConfig = {
  input: 'src/index.ts',
  external: [],
};

// Browser-specific configuration
const browserConfig = {
  ...baseConfig,
  output: [
    {
      file: 'dist/index.browser.js',
      format: 'esm',
      sourcemap: true,
    },
    {
      file: 'dist/index.browser.cjs',
      format: 'cjs',
      sourcemap: true,
    },
  ],
  plugins: [
    resolve({ browser: true }),
    commonjs(),
    typescript({
      tsconfig: './tsconfig.build.json',
      sourceMap: true,
      inlineSources: true,
    }),
  ],
};

// Node.js-specific configuration
const nodeConfig = {
  ...baseConfig,
  output: [
    {
      file: 'dist/index.node.js',
      format: 'esm',
      sourcemap: true,
    },
    {
      file: 'dist/index.node.cjs',
      format: 'cjs',
      sourcemap: true,
    },
  ],
  plugins: [
    resolve({ browser: false }),
    commonjs(),
    typescript({
      tsconfig: './tsconfig.build.json',
      sourceMap: true,
      inlineSources: true,
    }),
  ],
};

// Default configuration (for backward compatibility)
const defaultConfig = {
  ...baseConfig,
  output: [
    {
      file: 'dist/index.js',
      format: 'esm',
      sourcemap: true,
    },
    {
      file: 'dist/index.cjs',
      format: 'cjs',
      sourcemap: true,
    },
  ],
  plugins: [
    resolve(),
    commonjs(),
    typescript({
      tsconfig: './tsconfig.build.json',
      sourceMap: true,
      inlineSources: true,
    }),
  ],
};

export default [browserConfig, nodeConfig, defaultConfig];
