QT += network

HEADERS += \
# Models
    $${PWD}/OAIResourceHealthMetadata.h \
    $${PWD}/OAIResourceHealthMetadataCollection.h \
    $${PWD}/OAIResourceHealthMetadata_List_default_response.h \
    $${PWD}/OAIResourceHealthMetadata_List_default_response_error.h \
    $${PWD}/OAIResourceHealthMetadata_List_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIResourceHealthMetadataApi.h \
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
    $${PWD}/OAIResourceHealthMetadata.cpp \
    $${PWD}/OAIResourceHealthMetadataCollection.cpp \
    $${PWD}/OAIResourceHealthMetadata_List_default_response.cpp \
    $${PWD}/OAIResourceHealthMetadata_List_default_response_error.cpp \
    $${PWD}/OAIResourceHealthMetadata_List_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIResourceHealthMetadataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
