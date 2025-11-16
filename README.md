# 🚀 Google Cloud Storage AI Agent

A comprehensive, intelligent Google Cloud Storage management agent powered by Google's Agent Development Kit (ADK) and Gemini 2.0 Flash. This agent provides natural language interaction for all aspects of Google Cloud Storage management, from basic operations to advanced analytics and automation.

## 🌟 Features

### 🏗️ **Core Storage Management**
- **Bucket Operations**: Create, delete, list, and configure storage buckets
- **Object Management**: Upload, download, delete, rename, copy, and manage objects
- **Advanced Metadata**: Get detailed object and bucket information
- **Versioning Control**: Enable/disable versioning and restore object versions

### 🔐 **Security & Access Control**
- **IAM Management**: Add/remove bucket members with specific roles
- **ACL Management**: Object-level access control lists
- **Public Access Control**: Enable/disable public access
- **Security Auditing**: Comprehensive access pattern analysis
- **Uniform Bucket Level Access**: Configure advanced access controls

### 📊 **Monitoring & Analytics**
- **Usage Metrics**: Detailed bucket usage statistics and breakdowns
- **Cost Analysis**: Real-time cost estimation and optimization suggestions
- **Activity Monitoring**: Access log analysis and pattern recognition
- **Performance Insights**: Storage efficiency recommendations

### 🌐 **Website Hosting** ⭐ **FIXED**
- **Static Site Hosting**: Enable/disable website hosting with proper public access
- **Asset Management**: Upload website assets with proper content types
- **CORS Configuration**: Cross-origin request setup
- **Cache Control**: Performance optimization headers
- **Fix Applied**: Website hosting now properly configures IAM policies and CORS

### 🚀 **Advanced Operations**
- **Directory Synchronization**: Sync local directories to buckets
- **Backup & Migration**: Cross-bucket backup and region migration
- **Automated Archiving**: Archive old objects to reduce costs
- **Scheduled Cleanup**: Periodic maintenance and cleanup tasks
- **Cloud Function Integration**: Event-driven automation

### 🧠 **AI-Powered Intelligence**
- **Natural Language Processing**: Understand complex requests in plain English
- **Cost Optimization**: AI-powered storage class recommendations
- **Usage Pattern Analysis**: Intelligent insights and suggestions
- **Automated Decision Making**: Smart recommendations based on usage patterns

## 🛠️ Installation

### Prerequisites
- Python 3.13.3
- Google Cloud Project with Storage API enabled
- Service Account with Storage Admin permissions
- Google ADK (Agent Development Kit)

### Setup

1. **Navigate to project directory**
```bash
cd ~/Documents/After-graduation/Multi-Cloud-ai/GCP-Cloudmate-ai/bucket_storage_agent
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
# source venv/bin/activate    # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file:
```bash
cat > .env << 'EOF'
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=./service-account-key.json
EOF
```

5. **Set up Google Cloud credentials**

- Go to [GCP Console](https://console.cloud.google.com)
- IAM & Admin > Service Accounts > Create Service Account
- Grant "Storage Admin" role
- Create JSON key and save as `service-account-key.json`
- Place in the `bucket_storage_agent/` directory

6. **Test setup**
```bash
python test_auth.py
```

## 🚀 Quick Start

### Basic Usage

```python
from agent import root_agent
from google.adk.runners import Runner

# Initialize the agent
runner = Runner(root_agent)

# Example: Create a bucket
response = runner.run("Create a bucket named 'my-storage-bucket' in the US region")

# Example: Upload a file
response = runner.run("Upload the file 'document.pdf' to my-storage-bucket")

# Example: Get cost analysis
response = runner.run("Analyze the costs for my-storage-bucket and suggest optimizations")
```

### Natural Language Examples

The agent understands complex requests in natural language:

```python
# Complex operations
runner.run("Create a bucket for my website, enable hosting, upload my HTML files, and set up CORS")

# Cost optimization
runner.run("Analyze my storage usage and recommend cheaper storage classes for old files")

# Security auditing
runner.run("Audit my bucket permissions and show me any security issues")

# Backup operations
runner.run("Backup my production bucket to a different region for disaster recovery")

# Automated cleanup
runner.run("Archive all files older than 1 year to reduce costs")
```

### Direct Function Calls

```python
from tools import (
    create_storage_bucket,
    upload_object,
    enable_website_hosting,
    view_bucket_usage
)

# Create bucket
create_storage_bucket("my-bucket", location="US", storage_class="STANDARD")

# Upload file
upload_object("my-bucket", "./file.txt", "file.txt")

# Enable website hosting (FIXED - now works!)
result = enable_website_hosting("my-bucket", "index.html", "404.html")
print(result["website_config"]["website_url"])  # Get website URL

# View usage
view_bucket_usage("my-bucket")
```

## 📚 API Reference

### Bucket Management

| Function | Description | Example |
|----------|-------------|---------|
| `create_storage_bucket` | Create a new bucket | `create_storage_bucket("my-bucket", "US")` |
| `get_bucket_details` | Get comprehensive bucket info | `get_bucket_details("my-bucket")` |
| `update_bucket_configuration` | Update bucket settings | `update_bucket_configuration("my-bucket", storage_class="NEARLINE")` |
| `view_bucket_usage` | Get usage statistics | `view_bucket_usage("my-bucket")` |
| `delete_storage_bucket` | Delete a bucket | `delete_storage_bucket("my-bucket", force_delete_objects=True)` |

### Object Operations

| Function | Description | Example |
|----------|-------------|---------|
| `upload_object` | Upload a file | `upload_object("my-bucket", "./file.txt", "file.txt")` |
| `download_object` | Download a file | `download_object("my-bucket", "file.txt", "./local/")` |
| `list_objects` | List bucket contents | `list_objects("my-bucket", prefix="documents/")` |
| `generate_signed_url` | Create temporary access link | `generate_signed_url("my-bucket", "file.txt", 24)` |
| `delete_object` | Delete an object | `delete_object("my-bucket", "file.txt")` |
| `copy_object` | Copy object | `copy_object("my-bucket", "file.txt", "copy.txt")` |

### Website Hosting (FIXED)

| Function | Description | Example |
|----------|-------------|---------|
| `enable_website_hosting` | Enable static website hosting | `enable_website_hosting("my-bucket", "index.html")` |
| `disable_website_hosting` | Disable website hosting | `disable_website_hosting("my-bucket")` |
| `set_cors_configuration` | Configure CORS | `set_cors_configuration("my-bucket", ["*"])` |
| `upload_website_assets` | Upload website files | `upload_website_assets("my-bucket", "./website/")` |

### Advanced Features

| Function | Description | Example |
|----------|-------------|---------|
| `recommend_storage_class` | Get cost optimization suggestions | `recommend_storage_class("my-bucket")` |
| `summarize_bucket_status` | Get comprehensive bucket summary | `summarize_bucket_status("my-bucket")` |
| `audit_bucket_access` | Security and access analysis | `audit_bucket_access("my-bucket")` |
| `backup_bucket_to_another_bucket` | Cross-bucket backup | `backup_bucket_to_another_bucket("source", "backup")` |
| `view_bucket_cost_estimate` | Estimate costs | `view_bucket_cost_estimate("my-bucket")` |

## 🎯 Use Cases

### 1. **Website Hosting**
```python
# Complete website setup
runner.run("""
Create a bucket for my website, enable hosting, 
upload my HTML/CSS/JS files, configure CORS, 
and set up cache control for optimal performance
""")
```

### 2. **Data Backup & Archival**
```python
# Automated backup and archival
runner.run("""
Backup my production data to a different region,
archive files older than 6 months to reduce costs,
and set up automatic cleanup for temporary files
""")
```

### 3. **Cost Optimization**
```python
# Intelligent cost management
runner.run("""
Analyze my storage costs, identify expensive storage classes,
recommend optimizations, and show me potential savings
""")
```

### 4. **Security & Compliance**
```python
# Security auditing
runner.run("""
Audit my bucket permissions, check for public access,
review IAM policies, and provide security recommendations
""")
```

## 📁 Project Structure

```
bucket_storage_agent/
├── agent.py                      # Agent configuration with Gemini 2.0
├── tools.py                      # 70+ GCS operations (FIXED)
├── requirements.txt              # Python dependencies
├── .env                          # Environment configuration (create this)
├── service-account-key.json      # GCP credentials (create this)
├── create_env.py                 # Helper to create .env
├── env_template.txt              # Environment template
├── setup_service_account.sh      # Service account setup script
├── test_auth.py                  # Test authentication
├── test_bucket_access.py         # Test bucket operations
├── test_object_acl.py            # Test ACL operations
├── test_queries.txt              # Sample test queries
└── __pycache__/                  # Python cache
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_CLOUD_PROJECT` | Your GCP project ID | Yes |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to service account key | Yes |

### Agent Configuration

The agent is configured with:
- **Model**: Gemini 2.0 Flash Experimental
- **Capabilities**: 70+ storage management functions
- **Intelligence**: Natural language processing and reasoning
- **Optimization**: AI-powered cost and performance recommendations

## 🧪 Testing

### Quick Test (5 Minutes)

```python
from agent import root_agent
from google.adk.runners import Runner

runner = Runner(root_agent)

# Test 1: Create bucket
runner.run("Create a bucket called test-bucket-123")

# Test 2: Upload file
runner.run("Upload index.html to test-bucket-123")

# Test 3: Enable website hosting (CRITICAL TEST)
runner.run("Enable website hosting on test-bucket-123 with index.html")

# Test 4: Get URL and open in browser
response = runner.run("What's the URL of my website?")
# Open the URL in browser - should work (no 403 error!)

# Test 5: Cleanup
runner.run("Delete test-bucket-123 and all contents")
```

### Natural Language Test Prompts

See `QUICK_TEST_PROMPTS.md` for comprehensive testing prompts covering:
- Basic bucket operations (create, list, delete)
- Object operations (upload, download, copy, rename)
- Website hosting (enable, configure, disable)
- Permissions (public access, IAM, ACL)
- Monitoring (usage, costs, metrics)
- Advanced features (versioning, lifecycle, migration)

## 📊 Performance & Monitoring

### Built-in Analytics
- **Usage Metrics**: Object count, storage size, access patterns
- **Cost Analysis**: Real-time cost estimation and optimization
- **Performance Monitoring**: Activity analysis and recommendations
- **Security Auditing**: Access pattern analysis and security insights

### Monitoring Features
```python
# Enable comprehensive monitoring
runner.run("""
Enable request logging for my bucket,
set up activity monitoring,
and connect to BigQuery for advanced analytics
""")
```

## 🛡️ Security Features

### Access Control
- **IAM Management**: Fine-grained permission control
- **ACL Management**: Object-level access control
- **Public Access Prevention**: Security-first configurations
- **Audit Logging**: Comprehensive access tracking

### Security Best Practices
- **Uniform Bucket Level Access**: Enhanced security model
- **Encryption**: Default encryption for all objects
- **Access Auditing**: Regular security assessments
- **Compliance**: Built-in compliance monitoring

## 💰 Cost Optimization

### Intelligent Recommendations
- **Storage Class Optimization**: Automatic recommendations based on access patterns
- **Lifecycle Management**: Automated archival and deletion
- **Cost Analysis**: Real-time cost estimation and savings projections
- **Usage Optimization**: Efficiency recommendations

### Example Cost Optimization
```python
# Get cost optimization recommendations
response = runner.run("""
Analyze my storage costs and provide recommendations:
- Which files should be moved to cheaper storage classes?
- What's my potential monthly savings?
- How can I optimize my storage lifecycle?
""")
```

## 🚀 Advanced Operations

### Automation Features
- **Scheduled Tasks**: Periodic cleanup and maintenance
- **Event-Driven**: Cloud Function integration
- **Cross-Region Migration**: Automated data migration
- **Backup Automation**: Regular backup scheduling

### Enterprise Features
- **Multi-Bucket Management**: Manage multiple buckets simultaneously
- **Cross-Project Operations**: Work across different GCP projects
- **Compliance Reporting**: Generate compliance and audit reports
- **Integration**: BigQuery, Cloud Functions, and other GCP services

## 🔧 Troubleshooting

### Authentication Error
```bash
# Check .env file exists and has correct values
cat .env

# Test authentication
python test_auth.py
```

### Website Hosting 403 Error
- Ensure you're using the **FIXED** `tools.py` from this package
- The fix automatically configures public access and CORS
- Wait 1-2 minutes for IAM changes to propagate

### Module Not Found
```bash
# Ensure virtual environment is activated
source venv/Scripts/activate  # Windows
source venv/bin/activate      # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt
```

### Permission Denied
- Verify service account has "Storage Admin" role
- Check Cloud Storage API is enabled
- Ensure service account key is valid and not expired

## 📈 What's Fixed

### Website Hosting Fix (Critical)

The website hosting functionality had **three critical issues** that are now fixed:

1. **❌ Wrong bucket retrieval method** → ✅ Now uses `client.get_bucket()`
2. **❌ Deprecated API usage** → ✅ Now uses `bucket.configure_website()`
3. **❌ Missing public access** → ✅ Now configures IAM policy for public access
4. **❌ Missing CORS headers** → ✅ Now sets proper CORS configuration

**Result**: Website hosting now works correctly with publicly accessible URLs!

For detailed information about the fix:
- See `CHANGES_APPLIED.md` for what was changed
- See `BEFORE_AFTER_COMPARISON.md` for code comparison
- See `WEBSITE_HOSTING_FIX_GUIDE.md` for technical details

## 📚 Documentation

- **`README.md`** - This file (main documentation)
- **`QUICKSTART.md`** - 5-minute setup guide
- **`QUICK_TEST_PROMPTS.md`** - Natural language test prompts
- **`NATURAL_LANGUAGE_TEST_PROMPTS.md`** - Complete testing guide (36+ tests)
- **`CHANGES_APPLIED.md`** - What was fixed in website hosting
- **`TESTING_GUIDE.md`** - How to test all features
- **`MASTER_INDEX.md`** - Complete documentation index

## 🤝 Contributing

We welcome contributions! 

### Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd bucket_storage_agent

# Create virtual environment
python -m venv venv
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_auth.py
python test_bucket_access.py
```

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 Ngoga Alexis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 🙏 Acknowledgments

- **Google Cloud**: For providing the Storage API and infrastructure
- **Google ADK**: For the Agent Development Kit framework
- **Gemini 2.0**: For the advanced language model capabilities
- **Open Source Community**: For the libraries and tools that made this possible

## 📞 Support

- **Documentation**: See docs files in this repository
- **Testing**: `QUICK_TEST_PROMPTS.md` for test prompts
- **Issues**: Check troubleshooting section above
- **GCP Docs**: https://cloud.google.com/storage/docs

## 🌟 Star the Repository

If you find this project helpful, please give it a star! ⭐

---

**Built with ❤️ by Ngoga Alexis**

**Last Updated**: November 2024

**Status**: ✅ Production Ready with Fixed Website Hosting

*This project demonstrates the power of AI-driven cloud management and showcases the capabilities of Google's Agent Development Kit in creating intelligent, natural language interfaces for complex cloud operations.*