QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiskMigrationJob.h \
    $${PWD}/OAIDiskMigrationJobList.h \
    $${PWD}/OAIDiskMigrationJobProperties.h \
    $${PWD}/OAIDiskMigrationJobs_Create_request_inner.h \
    $${PWD}/OAIDiskMigrationJobs_Create_request_inner_properties.h \
    $${PWD}/OAIDiskMigrationJobs_Get_200_response.h \
    $${PWD}/OAIDiskMigrationJobs_List_200_response.h \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner.h \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner_properties.h \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner_properties_subtasks_inner.h \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner_properties_subtasks_inner_properties.h \
    $${PWD}/OAIMigrationJobStatus.h \
    $${PWD}/OAIMigrationSubTask.h \
    $${PWD}/OAIMigrationSubTaskProperties.h \
    $${PWD}/OAIMigrationSubTaskStatus.h \
# APIs
    $${PWD}/OAIDiskMigrationJobsApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIDiskMigrationJob.cpp \
    $${PWD}/OAIDiskMigrationJobList.cpp \
    $${PWD}/OAIDiskMigrationJobProperties.cpp \
    $${PWD}/OAIDiskMigrationJobs_Create_request_inner.cpp \
    $${PWD}/OAIDiskMigrationJobs_Create_request_inner_properties.cpp \
    $${PWD}/OAIDiskMigrationJobs_Get_200_response.cpp \
    $${PWD}/OAIDiskMigrationJobs_List_200_response.cpp \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner.cpp \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner_properties_subtasks_inner.cpp \
    $${PWD}/OAIDiskMigrationJobs_List_200_response_value_inner_properties_subtasks_inner_properties.cpp \
    $${PWD}/OAIMigrationJobStatus.cpp \
    $${PWD}/OAIMigrationSubTask.cpp \
    $${PWD}/OAIMigrationSubTaskProperties.cpp \
    $${PWD}/OAIMigrationSubTaskStatus.cpp \
# APIs
    $${PWD}/OAIDiskMigrationJobsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
