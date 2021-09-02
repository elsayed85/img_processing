<?php

use App\Services\ImageProcessing\Processor;

$router->get("py", function () {
    $processor = new Processor();
    $url = "https://imgmk.lotteautoauction.net/AU_INSP/202109/KS202109010057.JPG";

    try {
        $output = $processor->process("main.py", [$url]);
    } catch (\Throwable $th) {
        return response()->json([
            'error' => $th->getMessage()
        ]);
    }

    if (isJson($output)) {
        $output = json_decode($output, true);
        dd($output);
    }
});
