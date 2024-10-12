QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiVersionSetCollection.h \
    $${PWD}/OAIApiVersionSetContract.h \
    $${PWD}/OAIApiVersionSetContractProperties.h \
    $${PWD}/OAIApiVersionSetEntityBase.h \
    $${PWD}/OAIApiVersionSetUpdateParameters.h \
    $${PWD}/OAIApiVersionSetUpdateParametersProperties.h \
    $${PWD}/OAIApiVersionSet_ListByService_default_response.h \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error.h \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIApiVersionSetsApi.h \
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
    $${PWD}/OAIApiVersionSetCollection.cpp \
    $${PWD}/OAIApiVersionSetContract.cpp \
    $${PWD}/OAIApiVersionSetContractProperties.cpp \
    $${PWD}/OAIApiVersionSetEntityBase.cpp \
    $${PWD}/OAIApiVersionSetUpdateParameters.cpp \
    $${PWD}/OAIApiVersionSetUpdateParametersProperties.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_default_response.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error.cpp \
    $${PWD}/OAIApiVersionSet_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIApiVersionSetsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
