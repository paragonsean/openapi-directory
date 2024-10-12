QT += network

HEADERS += \
# Models
    $${PWD}/OAIFindFormByFormName_200_response.h \
    $${PWD}/OAIFindFormByFormName_404_response.h \
    $${PWD}/OAIFindFormByFormName_404_response_errors_inner.h \
    $${PWD}/OAIFindForms_200_response.h \
    $${PWD}/OAIFindForms_401_response.h \
    $${PWD}/OAIFindForms_429_response.h \
    $${PWD}/OAIFormShow.h \
    $${PWD}/OAIFormShow_attributes.h \
    $${PWD}/OAIFormShow_attributes_benefit_categories_inner.h \
    $${PWD}/OAIFormShow_attributes_versions_inner.h \
    $${PWD}/OAIFormsIndex.h \
    $${PWD}/OAIFormsIndex_attributes.h \
# APIs
    $${PWD}/OAIFormsApi.h \
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
    $${PWD}/OAIFindFormByFormName_200_response.cpp \
    $${PWD}/OAIFindFormByFormName_404_response.cpp \
    $${PWD}/OAIFindFormByFormName_404_response_errors_inner.cpp \
    $${PWD}/OAIFindForms_200_response.cpp \
    $${PWD}/OAIFindForms_401_response.cpp \
    $${PWD}/OAIFindForms_429_response.cpp \
    $${PWD}/OAIFormShow.cpp \
    $${PWD}/OAIFormShow_attributes.cpp \
    $${PWD}/OAIFormShow_attributes_benefit_categories_inner.cpp \
    $${PWD}/OAIFormShow_attributes_versions_inner.cpp \
    $${PWD}/OAIFormsIndex.cpp \
    $${PWD}/OAIFormsIndex_attributes.cpp \
# APIs
    $${PWD}/OAIFormsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
