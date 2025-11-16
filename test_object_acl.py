#!/usr/bin/env python3
"""
Test object ACL access for GCP Storage Agent
"""

import os
from dotenv import load_dotenv
from google.auth import default
from google.cloud import storage

def test_object_acl(bucket_name, object_name):
    """Test ACL access for a specific object."""
    
    print(f"🔍 Testing ACL access for object: {bucket_name}/{object_name}")
    print("=" * 60)
    
    # Load environment variables
    load_dotenv()
    
    # Check environment variables
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    
    if not project_id:
        print("❌ ERROR: GOOGLE_CLOUD_PROJECT not set")
        return False
    
    if not creds_path or not os.path.exists(creds_path):
        print("❌ ERROR: GOOGLE_APPLICATION_CREDENTIALS not set or file not found")
        return False
    
    print(f"📋 Project: {project_id}")
    print(f"🔑 Credentials: {creds_path}")
    
    try:
        # Set up client
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = creds_path
        credentials, auth_project = default()
        if auth_project:
            project_id = auth_project
        
        client = storage.Client(project=project_id, credentials=credentials)
        bucket = client.bucket(bucket_name)
        
        print(f"\n🔍 Testing bucket existence...")
        
        # Test 1: Check if bucket exists
        if not bucket.exists():
            print(f"❌ Bucket '{bucket_name}' does not exist")
            return False
        
        print(f"✅ Bucket '{bucket_name}' exists")
        
        # Test 2: Check if object exists
        print(f"\n🔍 Testing object existence...")
        blob = bucket.blob(object_name)
        
        if not blob.exists():
            print(f"❌ Object '{object_name}' does not exist in bucket '{bucket_name}'")
            return False
        
        print(f"✅ Object '{object_name}' exists")
        
        # Test 3: Check basic object access
        print(f"\n🔍 Testing basic object access...")
        try:
            blob.reload()
            print(f"✅ Basic object access works")
            print(f"📋 Object size: {blob.size} bytes")
            print(f"📋 Content type: {blob.content_type}")
        except Exception as e:
            print(f"❌ Basic object access failed: {e}")
            return False
        
        # Test 4: Check ACL access
        print(f"\n🔍 Testing ACL access...")
        try:
            acl_entries = []
            for entry in blob.acl:
                acl_entries.append({
                    "entity": str(entry.entity),
                    "role": str(entry.role)
                })
            
            print(f"✅ ACL access works")
            print(f"📋 Found {len(acl_entries)} ACL entries:")
            
            if acl_entries:
                for i, entry in enumerate(acl_entries, 1):
                    print(f"   {i}. Entity: {entry['entity']}, Role: {entry['role']}")
            else:
                print("   No ACL entries found (object uses bucket-level permissions)")
                
        except Exception as e:
            print(f"❌ ACL access failed: {e}")
            print("💡 This might be due to:")
            print("   - Insufficient permissions (need 'storage.objects.getIamPolicy')")
            print("   - Object doesn't have ACL configured")
            print("   - Bucket has uniform bucket-level access enabled")
            return False
        
        print(f"\n🎉 All tests passed! ACL access for '{object_name}' is working.")
        return True
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False

def main():
    """Test ACL access for a specific object."""
    
    bucket_name = input("Enter bucket name: ").strip()
    object_name = input("Enter object name: ").strip()
    
    if not bucket_name or not object_name:
        print("❌ Please provide both bucket name and object name")
        return
    
    print(f"\n🧪 Testing ACL access for {bucket_name}/{object_name}")
    print("=" * 60)
    
    test_object_acl(bucket_name, object_name)

if __name__ == "__main__":
    main()





