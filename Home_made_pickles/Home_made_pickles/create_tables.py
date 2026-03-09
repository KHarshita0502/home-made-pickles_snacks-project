import boto3

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

def create_users_table():
    """Create users table with username as partition key"""
    try:
        table = dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'  # String
                }
            ],
            BillingMode='PAY_PER_REQUEST'  # On-demand pricing
        )

        # Wait for table to be created
        table.wait_until_exists()
        print("✅ Users table created successfully!")
        return table

    except Exception as e:
        print(f"❌ Error creating users table: {str(e)}")
        return None

def create_orders_table():
    """Create orders table with order_id as partition key"""
    try:
        table = dynamodb.create_table(
            TableName='orders',
            KeySchema=[
                {
                    'AttributeName': 'order_id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'order_id',
                    'AttributeType': 'S'  # String
                }
            ],
            BillingMode='PAY_PER_REQUEST'  # On-demand pricing
        )

        # Wait for table to be created
        table.wait_until_exists()
        print("✅ Orders table created successfully!")
        return table

    except Exception as e:
        print(f"❌ Error creating orders table: {str(e)}")
        return None

if __name__ == "__main__":
    print("Creating DynamoDB tables...")

    users_table = create_users_table()
    orders_table = create_orders_table()

    if users_table and orders_table:
        print("\n🎉 All tables created successfully!")
        print(f"Users table status: {users_table.table_status}")
        print(f"Orders table status: {orders_table.table_status}")
    else:
        print("\n❌ Some tables failed to create. Check your AWS credentials and permissions.")