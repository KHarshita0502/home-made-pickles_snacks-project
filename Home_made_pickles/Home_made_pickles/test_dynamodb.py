import boto3

# Test DynamoDB connection and table existence
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def test_dynamodb_connection():
    try:
        # List all tables
        client = boto3.client('dynamodb', region_name='us-east-1')
        response = client.list_tables()
        tables = response.get('TableNames', [])

        print(f"Available tables: {tables}")

        # Check if our tables exist
        if 'users' in tables:
            print("✅ Users table exists")
        else:
            print("❌ Users table does not exist")

        if 'orders' in tables:
            print("✅ Orders table exists")
        else:
            print("❌ Orders table does not exist")

        # Test table access
        if 'users' in tables:
            users_table = dynamodb.Table('users')
            print(f"Users table status: {users_table.table_status}")

        if 'orders' in tables:
            orders_table = dynamodb.Table('orders')
            print(f"Orders table status: {orders_table.table_status}")

    except Exception as e:
        print(f"❌ DynamoDB connection error: {str(e)}")

if __name__ == "__main__":
    test_dynamodb_connection()