QT += network

HEADERS += \
# Models
    $${PWD}/OAILibraryItem.h \
    $${PWD}/OAIOrganization.h \
    $${PWD}/OAIProject.h \
    $${PWD}/OAITechnologyArea.h \
    $${PWD}/OAI_api_projects__format__get_200_response.h \
    $${PWD}/file.h \
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
    $${PWD}/OAILibraryItem.cpp \
    $${PWD}/OAIOrganization.cpp \
    $${PWD}/OAIProject.cpp \
    $${PWD}/OAITechnologyArea.cpp \
    $${PWD}/OAI_api_projects__format__get_200_response.cpp \
    $${PWD}/file.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
