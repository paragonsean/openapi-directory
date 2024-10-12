QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureIaaSVMErrorInfo.h \
    $${PWD}/OAIAzureIaaSVMJob.h \
    $${PWD}/OAIAzureIaaSVMJobExtendedInfo.h \
    $${PWD}/OAIAzureIaaSVMJobTaskDetails.h \
    $${PWD}/OAIDpmErrorInfo.h \
    $${PWD}/OAIDpmJob.h \
    $${PWD}/OAIDpmJobExtendedInfo.h \
    $${PWD}/OAIDpmJobTaskDetails.h \
    $${PWD}/OAIJob.h \
    $${PWD}/OAIJobQueryObject.h \
    $${PWD}/OAIJobResource.h \
    $${PWD}/OAIJobResourceList.h \
    $${PWD}/OAIMabErrorInfo.h \
    $${PWD}/OAIMabJob.h \
    $${PWD}/OAIMabJobExtendedInfo.h \
    $${PWD}/OAIMabJobTaskDetails.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceList.h \
# APIs
    $${PWD}/OAIBackupJobsApi.h \
    $${PWD}/OAIJobDetailsApi.h \
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
    $${PWD}/OAIAzureIaaSVMErrorInfo.cpp \
    $${PWD}/OAIAzureIaaSVMJob.cpp \
    $${PWD}/OAIAzureIaaSVMJobExtendedInfo.cpp \
    $${PWD}/OAIAzureIaaSVMJobTaskDetails.cpp \
    $${PWD}/OAIDpmErrorInfo.cpp \
    $${PWD}/OAIDpmJob.cpp \
    $${PWD}/OAIDpmJobExtendedInfo.cpp \
    $${PWD}/OAIDpmJobTaskDetails.cpp \
    $${PWD}/OAIJob.cpp \
    $${PWD}/OAIJobQueryObject.cpp \
    $${PWD}/OAIJobResource.cpp \
    $${PWD}/OAIJobResourceList.cpp \
    $${PWD}/OAIMabErrorInfo.cpp \
    $${PWD}/OAIMabJob.cpp \
    $${PWD}/OAIMabJobExtendedInfo.cpp \
    $${PWD}/OAIMabJobTaskDetails.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceList.cpp \
# APIs
    $${PWD}/OAIBackupJobsApi.cpp \
    $${PWD}/OAIJobDetailsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
