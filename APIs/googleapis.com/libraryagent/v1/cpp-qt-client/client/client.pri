QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleExampleLibraryagentV1Book.h \
    $${PWD}/OAIGoogleExampleLibraryagentV1ListBooksResponse.h \
    $${PWD}/OAIGoogleExampleLibraryagentV1ListShelvesResponse.h \
    $${PWD}/OAIGoogleExampleLibraryagentV1Shelf.h \
# APIs
    $${PWD}/OAIShelvesApi.h \
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
    $${PWD}/OAIGoogleExampleLibraryagentV1Book.cpp \
    $${PWD}/OAIGoogleExampleLibraryagentV1ListBooksResponse.cpp \
    $${PWD}/OAIGoogleExampleLibraryagentV1ListShelvesResponse.cpp \
    $${PWD}/OAIGoogleExampleLibraryagentV1Shelf.cpp \
# APIs
    $${PWD}/OAIShelvesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
