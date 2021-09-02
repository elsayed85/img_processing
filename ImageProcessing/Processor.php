<?php

namespace App\Services\ImageProcessing;

use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;


class Processor
{
    public $path = "Services\ImageProcessing\Scripts";

    public function process(string $filename, array $parameters = [])
    {
        $process = new Process(array_merge(["python", app_path($this->path . '\\' . $filename)], $parameters));
        $process->run();
        $process->wait();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }

        return rtrim($process->getOutput(), "\n");
    }
}
