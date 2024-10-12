QT += network

HEADERS += \
# Models
    $${PWD}/OAIFigiResult.h \
    $${PWD}/OAIMappingJob.h \
    $${PWD}/OAIMappingJobResult.h \
    $${PWD}/OAIMappingJobResultFigiList.h \
    $${PWD}/OAIMappingJobResultFigiNotFound.h \
    $${PWD}/OAIMappingJob_idValue.h \
    $${PWD}/OAI_mapping_values__key__get_200_response.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIFigiResult.cpp \
    $${PWD}/OAIMappingJob.cpp \
    $${PWD}/OAIMappingJobResult.cpp \
    $${PWD}/OAIMappingJobResultFigiList.cpp \
    $${PWD}/OAIMappingJobResultFigiNotFound.cpp \
    $${PWD}/OAIMappingJob_idValue.cpp \
    $${PWD}/OAI_mapping_values__key__get_200_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
