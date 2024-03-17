import React, { useEffect } from 'react';
import { FilesetResolver, poseLandmarker } from '@mediapipe/tasks-vision';

const Vision = () => {

  // on page load, load the model
  // useEffect(() => {
  //   const setupVision = async () => {
  //     const vision = await FilesetResolver.forVisionTasks(
  //       'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@latest/wasm',
  //     );
  //     const poseLandmarker = await poseLandmarker.createFromOptions(vision, {
  //       baseOptions: {
  //         modelAssetPath: 'path/to/model',
  //       },
  //       runningMode: runningMode,
  //     });
  //   };
  //   setupVision();
  // }, []);

  return (
    <div>
      <div>
        <h1 className="text-3xl bg-slate-200 text-center p-4 mb-10">
          Computer Vision Program Test
        </h1>
      </div>
    </div>
  );
};

export default Vision;
