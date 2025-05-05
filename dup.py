# duplication_example.py
import logging
import time
import random
import os # Added unused import - not duplication, but Sonar might flag it

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- BLOCK 1: Configuration Loading ---
# This function simulates loading configuration data, perhaps from a primary source.
def load_config_from_file(filepath):
    """Loads configuration pretending to read from a file."""
    logging.info(f"Attempting to load configuration from {filepath}...")
    try:
        # Simulate I/O and parsing delay
        time.sleep(0.05)
        if not filepath or not filepath.endswith(".cfg"):
            logging.error(f"Invalid primary config path: {filepath}")
            raise ValueError("Invalid config file extension or path.")

        # Simulate reading and parsing data
        config_data = {
            'db_host': 'prod.db.internal',
            'db_port': 5432,
            'retries': 3,
            'timeout_ms': 5000,
            'feature_flags': ['new_ui', 'beta_feature_x'],
            'log_level': 'INFO'
        }
        logging.info(f"Successfully loaded configuration from {filepath}.")
        return config_data
    except Exception as e:
        logging.error(f"Failed to load config from {filepath}: {e}")
        # Fallback configuration on error
        logging.warning("Using fallback primary configuration.")
        return {
            'db_host': 'fallback.db.internal', 'db_port': 5432,
            'retries': 1, 'timeout_ms': 2000, 'feature_flags': [],
            'log_level': 'WARN'
        }

# --- BLOCK 2: Configuration Loading (Duplicated with minor changes) ---
# This function is almost identical to load_config_from_file, simulating
# loading from a backup source. SonarQube will likely flag this duplication.
def load_backup_config_from_file(backup_filepath):
    """Loads backup configuration pretending to read from a file."""
    logging.info(f"Attempting to load BACKUP configuration from {backup_filepath}...") # Minor change
    try:
        # Simulate I/O and parsing delay (identical)
        time.sleep(0.05)
        if not backup_filepath or not backup_filepath.endswith(".cfg.bak"): # Changed extension check
            logging.error(f"Invalid backup config path: {backup_filepath}") # Minor change
            raise ValueError("Invalid backup config file extension or path.") # Changed message slightly

        # Simulate reading and parsing data (slightly different values)
        config_data = {
            'db_host': 'backup.db.internal', # Changed value
            'db_port': 5433, # Changed value
            'retries': 5, # Changed value
            'timeout_ms': 7000, # Changed value
            'feature_flags': ['new_ui'], # Changed value
            'log_level': 'DEBUG' # Changed value
        }
        logging.info(f"Successfully loaded BACKUP configuration from {backup_filepath}.") # Minor change
        return config_data
    except Exception as e:
        logging.error(f"Failed to load BACKUP config from {backup_filepath}: {e}") # Minor change
        # Fallback configuration on error (also slightly different)
        logging.warning("Using fallback backup configuration.") # Minor change
        return {
            'db_host': 'fallback-backup.db.internal', 'db_port': 5432, # Changed value
            'retries': 1, 'timeout_ms': 2500, 'feature_flags': [], # Changed value
            'log_level': 'INFO' # Changed value
        }

# --- BLOCK 2.5: Configuration Loading (Duplicated with minor changes) ---
# This function is almost identical to load_config_from_file, simulating
# loading from a backup source. SonarQube will likely flag this duplication.
def load_backup_config_from_file2(backup_filepath):
    """Loads backup configuration pretending to read from a file."""
    logging.info(f"Attempting to load BACKUP configuration from {backup_filepath}...") # Minor change
    try:
        # Simulate I/O and parsing delay (identical)
        time.sleep(0.05)
        if not backup_filepath or not backup_filepath.endswith(".cfg.bak"): # Changed extension check
            logging.error(f"Invalid backup config path: {backup_filepath}") # Minor change
            raise ValueError("Invalid backup config file extension or path.") # Changed message slightly

        # Simulate reading and parsing data (slightly different values)
        config_data = {
            'db_host': 'backup.db.internal', # Changed value
            'db_port': 5433, # Changed value
            'retries': 5, # Changed value
            'timeout_ms': 7000, # Changed value
            'feature_flags': ['new_ui'], # Changed value
            'log_level': 'DEBUG' # Changed value
        }
        logging.info(f"Successfully loaded BACKUP configuration from {backup_filepath}.") # Minor change
        return config_data
    except Exception as e:
        logging.error(f"Failed to load BACKUP config from {backup_filepath}: {e}") # Minor change
        # Fallback configuration on error (also slightly different)
        logging.warning("Using fallback backup configuration.") # Minor change
        return {
            'db_host': 'fallback-backup.db.internal', 'db_port': 5432, # Changed value
            'retries': 1, 'timeout_ms': 2500, 'feature_flags': [], # Changed value
            'log_level': 'INFO' # Changed value
        }



# --- BLOCK 3: Data Processing Function A ---
# Simulates processing one type of data structure.
def process_data_type_a(data_a):
    """Processes data of type A."""
    item_id = data_a.get('id', 'UNKNOWN_A')
    logging.info(f"Processing Type A data for item {item_id}")
    value = data_a.get('value', 0)
    category = data_a.get('category', 'default')
    processed = False

    # --- Start Duplicated Processing Logic Block ---
    # This block of logic is very similar in process_data_type_b and process_data_type_c
    print(f"  STEP 1: Validating item {item_id}...")
    time.sleep(random.uniform(0.01, 0.03)) # Simulate work
    is_valid = True
    if value < 0:
        logging.warning(f"Item {item_id} (Type A) has negative value {value}. Marking as invalid for this example.")
        is_valid = False # Simplified validation logic

    if is_valid:
        print(f"  STEP 2: Applying transformation for category '{category}'...")
        time.sleep(random.uniform(0.02, 0.05)) # Simulate work
        # Specific transformation for Type A
        transformed_value = (value * 1.1) + 5

        print(f"  STEP 3: Performing persistence for item {item_id}...")
        time.sleep(random.uniform(0.03, 0.06)) # Simulate DB write/API call
        # Simulate save operation
        processed = True
        result = {'id': item_id, 'transformed': transformed_value, 'status': 'Processed Type A', 'category': category}
        logging.info(f"Finished processing Type A item {item_id} successfully.")
    else:
        logging.error(f"Validation failed for Type A item {item_id}.")
        result = {'id': item_id, 'status': 'Failed Validation A', 'category': category}
    # --- End Duplicated Processing Logic Block ---

    return result

# --- BLOCK 4: Data Processing Function B (Duplicated) ---
# Simulates processing another type of data structure, but the core logic
# inside is almost identical to process_data_type_a.
def process_data_type_b(data_b):
    """Processes data of type B."""
    item_id = data_b.get('record_id', 'UNKNOWN_B') # Different key used
    logging.info(f"Processing Type B data for item {item_id}") # Minor text change
    value = data_b.get('measurement', 0.0) # Different key used
    category = data_b.get('group', 'standard') # Different key used
    processed = False

    # --- Start Duplicated Processing Logic Block ---
    # This block should be flagged as duplicated with the one in process_data_type_a
    print(f"  STEP 1: Validating item {item_id}...") # Identical structure/calls
    time.sleep(random.uniform(0.01, 0.03)) # Simulate work (Identical)
    is_valid = True
    if value < 0: # Identical structure
        logging.warning(f"Item {item_id} (Type B) has negative value {value}. Marking as invalid for this example.") # Minor text change
        is_valid = False # Identical logic

    if is_valid:
        print(f"  STEP 2: Applying transformation for group '{category}'...") # Minor text change
        time.sleep(random.uniform(0.02, 0.05)) # Simulate work (Identical)
        # Specific transformation for Type B (DIFFERENT CALCULATION, but structure around it is same)
        transformed_value = (value * 0.9) - 2

        print(f"  STEP 3: Performing persistence for item {item_id}...") # Identical structure/calls
        time.sleep(random.uniform(0.03, 0.06)) # Simulate DB write/API call (Identical)
        # Simulate save operation (Identical)
        processed = True
        result = {'record_id': item_id, 'transformed': transformed_value, 'status': 'Processed Type B', 'group': category} # Uses different keys/status text
        logging.info(f"Finished processing Type B item {item_id} successfully.") # Minor text change
    else:
        logging.error(f"Validation failed for Type B item {item_id}.") # Minor text change
        result = {'record_id': item_id, 'status': 'Failed Validation B', 'group': category} # Uses different keys/status text
    # --- End Duplicated Processing Logic Block ---

    return result

# --- BLOCK 5: Data Processing Function C (More Duplication) ---
# Yet another processing function with the same core structure.
def process_data_type_c(data_c):
    """Processes data of type C."""
    item_id = data_c.get('entity_id', 'UNKNOWN_C') # Different key used
    logging.info(f"Processing Type C data for item {item_id}") # Minor text change
    value = data_c.get('score', 0.0) # Different key used
    category = data_c.get('tier', 'basic') # Different key used
    processed = False

    # --- Start Duplicated Processing Logic Block ---
    # This block should be flagged as duplicated with the ones above.
    print(f"  STEP 1: Validating item {item_id}...") # Identical structure/calls
    time.sleep(random.uniform(0.01, 0.03)) # Simulate work (Identical)
    is_valid = True
    if value < 10: # Slightly different validation condition, but structure is the same
        logging.warning(f"Item {item_id} (Type C) has low score {value}. Marking as invalid for this example.") # Minor text change
        is_valid = False # Identical logic

    if is_valid:
        print(f"  STEP 2: Applying transformation for tier '{category}'...") # Minor text change
        time.sleep(random.uniform(0.02, 0.05)) # Simulate work (Identical)
        # Specific transformation for Type C (DIFFERENT CALCULATION)
        transformed_value = value + 100

        print(f"  STEP 3: Performing persistence for item {item_id}...") # Identical structure/calls
        time.sleep(random.uniform(0.03, 0.06)) # Simulate DB write/API call (Identical)
        # Simulate save operation (Identical)
        processed = True
        result = {'entity_id': item_id, 'transformed': transformed_value, 'status': 'Processed Type C', 'tier': category} # Uses different keys/status text
        logging.info(f"Finished processing Type C item {item_id} successfully.") # Minor text change
    else:
        logging.error(f"Validation failed for Type C item {item_id}.") # Minor text change
        result = {'entity_id': item_id, 'status': 'Failed Validation C', 'tier': category} # Uses different keys/status text
    # --- End Duplicated Processing Logic Block ---

    return result


if __name__ == "__main__":
    print("--- Loading Configurations ---")
    primary_config = load_config_from_file("production.cfg")
    backup_config = load_backup_config_from_file("production.cfg.bak")
    print(f"Primary Config Loaded: {primary_config.get('db_host')}")
    print(f"Backup Config Loaded: {backup_config.get('db_host')}")

    print("\n--- Processing Data Sets ---")
    data_set_a = [{'id': 'A001', 'value': 100, 'category': 'premium'}, {'id': 'A002', 'value': -50}]
    data_set_b = [{'record_id': 'B101', 'measurement': 25.5, 'group': 'standard'}, {'record_id': 'B102', 'measurement': 75.0, 'group': 'vip'}]
    data_set_c = [{'entity_id': 'C201', 'score': 30.0, 'tier': 'basic'}, {'entity_id': 'C202', 'score': 5.0, 'tier': 'advanced'}] # One item will fail validation

    results_a = [process_data_type_a(item) for item in data_set_a]
    results_b = [process_data_type_b(item) for item in data_set_b]
    results_c = [process_data_type_c(item) for item in data_set_c]

    print("\n--- Results ---")
    print("Type A Results:", results_a)
    print("Type B Results:", results_b)
    print("Type C Results:", results_c)

    print("\n--- Finished ---")
