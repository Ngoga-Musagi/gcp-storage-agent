# import os
# import uuid
# import json
# from google.adk.agents import Agent
# from google.adk.models.lite_llm import LiteLlm
# from google.adk.runners import Runner

# from .tools import (
#     # Basic bucket operations
#     create_storage_bucket,
#     delete_storage_bucket,
#     list_storage_buckets,  
    
#     # Bucket management
#     get_bucket_details,
#     update_bucket_configuration,
#     enable_versioning,
#     disable_versioning,
#     view_bucket_usage,
    
#     # Object operations
#     upload_object,
#     download_object,
#     delete_object,
#     rename_object,
#     copy_object,
#     list_objects,
#     get_object_metadata,
#     generate_signed_url,
    
#     # Permissions management
#     add_bucket_member,
#     remove_bucket_member,
#     list_bucket_permissions,
#     enable_public_access,
#     disable_public_access,
    
#     # Monitoring & optimization
#     view_bucket_metrics,
#     view_bucket_cost_estimate,
#     monitor_access_logs,
    
#     # Website hosting
#     enable_website_hosting,
#     disable_website_hosting,
#     set_website_main_page,
#     set_website_error_page,
#     upload_website_assets,
#     set_cors_configuration,
#     set_cache_control,
    
#     # Advanced features
#     connect_to_bigquery_dataset,
#     summarize_bucket_status,
#     recommend_storage_class,
    
#     # Bucket policy management
#     get_bucket_policy,
#     set_bucket_policy,
#     lock_bucket_policy,
#     get_bucket_iam_policy,
#     set_bucket_iam_policy,
#     add_bucket_label,
#     remove_bucket_label,
#     set_bucket_lifecycle_rules,
    
#     # Advanced object management
#     update_object_metadata,
#     set_object_acl,
#     get_object_acl,
#     restore_object_version,
    
#     # Advanced access & security
#     audit_bucket_access,
#     set_uniform_bucket_level_access,
    
#     # Advanced monitoring
#     enable_request_logging,
#     disable_request_logging,
#     analyze_bucket_activity,
    
#     # Advanced operations
#     sync_local_directory_to_bucket,
#     backup_bucket_to_another_bucket,
#     migrate_bucket_to_different_region,
#     trigger_cloud_function_on_event,
#     schedule_periodic_cleanup,
#     archive_old_objects,
# )

# # Define the agent
# root_agent = Agent(
#     name="gcp_storage_agent",
#     model="gemini-2.0-flash-exp",
#     description="Comprehensive Google Cloud Storage management agent with natural language interface for buckets, objects, permissions, monitoring, website hosting, and advanced analytics.",
#     instruction=(
#         "You are an advanced Google Cloud Storage management agent that provides comprehensive storage operations through natural language interaction. "
#         "You can help users manage every aspect of their Google Cloud Storage infrastructure with intelligent reasoning and cost optimization suggestions."
#         "\n\nYour comprehensive capabilities include:"
#         "\n\n🏗️ BUCKET MANAGEMENT:"
#         "\n- Create, delete, and list storage buckets with custom configurations"
#         "\n- Get detailed bucket metadata (location, storage class, labels, IAM policies, lifecycle rules)"
#         "\n- Update bucket configurations (storage class, versioning, labels, encryption)"
#         "\n- Enable/disable versioning for data protection"
#         "\n- View bucket usage statistics and storage breakdown"
#         "\n\n📁 OBJECT OPERATIONS:"
#         "\n- Upload, download, delete, rename, and copy objects"
#         "\n- List objects with filtering and pagination"
#         "\n- Get detailed object metadata and properties"
#         "\n- Generate signed URLs for secure temporary access"
#         "\n- Manage object metadata and content types"
#         "\n\n🔐 PERMISSIONS & SECURITY:"
#         "\n- Add/remove bucket members with specific IAM roles"
#         "\n- List and manage bucket permissions"
#         "\n- Enable/disable public access with security considerations"
#         "\n- Audit bucket access patterns and security"
#         "\n- Set uniform bucket-level access controls"
#         "\n\n🌐 WEBSITE HOSTING:"
#         "\n- Enable/disable static website hosting"
#         "\n- Configure main page and error page settings"
#         "\n- Upload website assets (HTML, CSS, JS, images)"
#         "\n- Set CORS configuration for cross-origin requests"
#         "\n- Configure cache control for optimal performance"
#         "\n\n📊 MONITORING & ANALYTICS:"
#         "\n- View comprehensive bucket metrics and usage statistics"
#         "\n- Analyze cost estimates and provide optimization recommendations"
#         "\n- Monitor access logs and activity patterns"
#         "\n- Connect to BigQuery for advanced analytics"
#         "\n- Generate intelligent storage recommendations"
#         "\n\n🔧 ADVANCED FEATURES:"
#         "\n- Bucket policy management and IAM policy configuration"
#         "\n- Lifecycle rules for automated data management"
#         "\n- Object versioning and restoration"
#         "\n- Cross-region backup and migration"
#         "\n- Cloud Function integration for event-driven automation"
#         "\n- Scheduled cleanup and archival processes"
#         "\n\n💡 INTELLIGENT REASONING:"
#         "\n- Analyze user requests and provide optimal solutions"
#         "\n- Suggest cost-effective storage strategies"
#         "\n- Recommend security best practices"
#         "\n- Provide step-by-step guidance for complex operations"
#         "\n- Offer proactive optimization suggestions"
#         "\n\nAlways prioritize security, cost-efficiency, and best practices. "
#         "When users ask for help, provide clear explanations of what you're doing and why. "
#         "For complex operations, break them down into manageable steps and confirm before proceeding. "
#         "Always consider the user's specific use case and provide tailored recommendations."
#     ),
#     tools=[
#         # Basic bucket operations
#         create_storage_bucket,
#         delete_storage_bucket,
#         list_storage_buckets,
        
#         # Bucket management
#         get_bucket_details,
#         update_bucket_configuration,
#         enable_versioning,
#         disable_versioning,
#         view_bucket_usage,
        
#         # Object operations
#         upload_object,
#         download_object,
#         delete_object,
#         rename_object,
#         copy_object,
#         list_objects,
#         get_object_metadata,
#         generate_signed_url,
        
#         # Permissions management
#         add_bucket_member,
#         remove_bucket_member,
#         list_bucket_permissions,
#         enable_public_access,
#         disable_public_access,
        
#         # Monitoring & optimization
#         view_bucket_metrics,
#         view_bucket_cost_estimate,
#         monitor_access_logs,
        
#         # Website hosting
#         enable_website_hosting,
#         disable_website_hosting,
#         set_website_main_page,
#         set_website_error_page,
#         upload_website_assets,
#         set_cors_configuration,
#         set_cache_control,
        
#         # Advanced features
#         connect_to_bigquery_dataset,
#         summarize_bucket_status,
#         recommend_storage_class,
        
#         # Bucket policy management
#         get_bucket_policy,
#         set_bucket_policy,
#         lock_bucket_policy,
#         get_bucket_iam_policy,
#         set_bucket_iam_policy,
#         add_bucket_label,
#         remove_bucket_label,
#         set_bucket_lifecycle_rules,
        
#         # Advanced object management
#         update_object_metadata,
#         set_object_acl,
#         get_object_acl,
#         restore_object_version,
        
#         # Advanced access & security
#         audit_bucket_access,
#         set_uniform_bucket_level_access,
        
#         # Advanced monitoring
#         enable_request_logging,
#         disable_request_logging,
#         analyze_bucket_activity,
        
#         # Advanced operations
#         sync_local_directory_to_bucket,
#         backup_bucket_to_another_bucket,
#         migrate_bucket_to_different_region,
#         trigger_cloud_function_on_event,
#         schedule_periodic_cleanup,
#         archive_old_objects,
#     ]
# )
import os
import uuid
import json
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner

from .tools import (
    # Basic bucket operations
    create_storage_bucket,
    delete_storage_bucket,
    list_storage_buckets,  
    
    # Bucket management
    get_bucket_details,
    update_bucket_configuration,
    enable_versioning,
    disable_versioning,
    view_bucket_usage,
    
    # Object operations
    upload_object,
    download_object,
    delete_object,
    rename_object,
    copy_object,
    list_objects,
    get_object_metadata,
    generate_signed_url,
    
    # Permissions management
    add_bucket_member,
    remove_bucket_member,
    list_bucket_permissions,
    enable_public_access,
    disable_public_access,
    
    # Monitoring & optimization
    view_bucket_metrics,
    view_bucket_cost_estimate,
    monitor_access_logs,
    
    # Website hosting
    enable_website_hosting,
    disable_website_hosting,
    set_website_main_page,
    set_website_error_page,
    upload_website_assets,
    set_cors_configuration,
    set_cache_control,
    
    # Advanced features
    connect_to_bigquery_dataset,
    summarize_bucket_status,
    recommend_storage_class,
    
    # Bucket policy management
    get_bucket_policy,
    set_bucket_policy,
    lock_bucket_policy,
    get_bucket_iam_policy,
    set_bucket_iam_policy,
    add_bucket_label,
    remove_bucket_label,
    set_bucket_lifecycle_rules,
    
    # Advanced object management
    update_object_metadata,
    set_object_acl,
    get_object_acl,
    restore_object_version,
    
    # Advanced access & security
    audit_bucket_access,
    set_uniform_bucket_level_access,
    
    # Advanced monitoring
    enable_request_logging,
    disable_request_logging,
    analyze_bucket_activity,
    
    # Advanced operations
    sync_local_directory_to_bucket,
    backup_bucket_to_another_bucket,
    migrate_bucket_to_different_region,
    trigger_cloud_function_on_event,
    schedule_periodic_cleanup,
    archive_old_objects,
)

# Define the agent
root_agent = Agent(
    name="gcp_storage_agent",
    model="gemini-2.0-flash-exp",
    description="Comprehensive Google Cloud Storage management agent with natural language interface for buckets, objects, permissions, monitoring, website hosting, and advanced analytics.",
    instruction=(
        "You are an advanced Google Cloud Storage management agent that provides comprehensive storage operations through natural language interaction. "
        "You can help users manage every aspect of their Google Cloud Storage infrastructure with intelligent reasoning and cost optimization suggestions."
        "\n\nYour comprehensive capabilities include:"
        "\n\n🏗️ BUCKET MANAGEMENT:"
        "\n- Create, delete, and list storage buckets with custom configurations"
        "\n- Get detailed bucket metadata (location, storage class, labels, IAM policies, lifecycle rules)"
        "\n- Update bucket configurations (storage class, versioning, labels, encryption)"
        "\n- Enable/disable versioning for data protection"
        "\n- View bucket usage statistics and storage breakdown"
        "\n\n📁 OBJECT OPERATIONS:"
        "\n- Upload, download, delete, rename, and copy objects"
        "\n- List objects with filtering and pagination"
        "\n- Get detailed object metadata and properties"
        "\n- Generate signed URLs for secure temporary access"
        "\n- Manage object metadata and content types"
        "\n\n🔐 PERMISSIONS & SECURITY:"
        "\n- Add/remove bucket members with specific IAM roles"
        "\n- List and manage bucket permissions"
        "\n- Enable/disable public access with security considerations"
        "\n- Audit bucket access patterns and security"
        "\n- Set uniform bucket-level access controls"
        "\n\n🌐 WEBSITE HOSTING:"
        "\n- Enable/disable static website hosting"
        "\n- Configure main page and error page settings"
        "\n- Upload website assets (HTML, CSS, JS, images)"
        "\n- Set CORS configuration for cross-origin requests"
        "\n- Configure cache control for optimal performance"
        "\n\n📊 MONITORING & ANALYTICS:"
        "\n- View comprehensive bucket metrics and usage statistics"
        "\n- Analyze cost estimates and provide optimization recommendations"
        "\n- Monitor access logs and activity patterns"
        "\n- Connect to BigQuery for advanced analytics"
        "\n- Generate intelligent storage recommendations"
        "\n\n🔧 ADVANCED FEATURES:"
        "\n- Bucket policy management and IAM policy configuration"
        "\n- Lifecycle rules for automated data management"
        "\n- Object versioning and restoration"
        "\n- Cross-region backup and migration"
        "\n- Cloud Function integration for event-driven automation"
        "\n- Scheduled cleanup and archival processes"
        "\n\n💡 INTELLIGENT REASONING:"
        "\n- Analyze user requests and provide optimal solutions"
        "\n- Suggest cost-effective storage strategies"
        "\n- Recommend security best practices"
        "\n- Provide step-by-step guidance for complex operations"
        "\n- Offer proactive optimization suggestions"
        "\n\nAlways prioritize security, cost-efficiency, and best practices. "
        "When users ask for help, provide clear explanations of what you're doing and why. "
        "For complex operations, break them down into manageable steps and confirm before proceeding. "
        "Always consider the user's specific use case and provide tailored recommendations."
    ),
    tools=[
        # Basic bucket operations
        create_storage_bucket,
        delete_storage_bucket,
        list_storage_buckets,
        
        # Bucket management
        get_bucket_details,
        update_bucket_configuration,
        enable_versioning,
        disable_versioning,
        view_bucket_usage,
        
        # Object operations
        upload_object,
        download_object,
        delete_object,
        rename_object,
        copy_object,
        list_objects,
        get_object_metadata,
        generate_signed_url,
        
        # Permissions management
        add_bucket_member,
        remove_bucket_member,
        list_bucket_permissions,
        enable_public_access,
        disable_public_access,
        
        # Monitoring & optimization
        view_bucket_metrics,
        view_bucket_cost_estimate,
        monitor_access_logs,
        
        # Website hosting
        enable_website_hosting,
        disable_website_hosting,
        set_website_main_page,
        set_website_error_page,
        upload_website_assets,
        set_cors_configuration,
        set_cache_control,
        
        # Advanced features
        connect_to_bigquery_dataset,
        summarize_bucket_status,
        recommend_storage_class,
        
        # Bucket policy management
        get_bucket_policy,
        set_bucket_policy,
        lock_bucket_policy,
        get_bucket_iam_policy,
        set_bucket_iam_policy,
        add_bucket_label,
        remove_bucket_label,
        set_bucket_lifecycle_rules,
        
        # Advanced object management
        update_object_metadata,
        set_object_acl,
        get_object_acl,
        restore_object_version,
        
        # Advanced access & security
        audit_bucket_access,
        set_uniform_bucket_level_access,
        
        # Advanced monitoring
        enable_request_logging,
        disable_request_logging,
        analyze_bucket_activity,
        
        # Advanced operations
        sync_local_directory_to_bucket,
        backup_bucket_to_another_bucket,
        migrate_bucket_to_different_region,
        trigger_cloud_function_on_event,
        schedule_periodic_cleanup,
        archive_old_objects,
    ]
)