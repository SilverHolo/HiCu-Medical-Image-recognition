import os

# Set number of runs
num_runs = 1

for i in range(1, num_runs + 1):
    print(f"Starting run No. {i} of {num_runs}")
    
    cmd = (
        "python /content/DN3HiCu/main.py "
        "--model MultiResCNN "
        "--vocab /content/DN3HiCu/data/mimic3/vocab.csv "
        "--decoder Hierarchical "
        "--loss ASL "
        "--asl_config 1,0,0.05 "
        "--Y 50 "
        "--data_path /content/DN3HiCu/data/mimic3/train_50.csv "
        "--MAX_LENGTH 4096 "
        "--embed_file /content/DN3HiCu/data/mimic3/processed_full_100.embed "
        "--tune_wordemb "
        "--batch_size 8 "
        "--lr 5e-5 "
        "--n_epochs 2,2,3,5,50 "
        "--criterion prec_at_8 "
        "--random_seed 0 "
        "--num_workers 1 "
    )

    os.system(cmd)

print(f"Completed all {num_runs} runs")
