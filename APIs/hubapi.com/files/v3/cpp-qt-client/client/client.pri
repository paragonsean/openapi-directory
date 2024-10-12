QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectionResponseFile.h \
    $${PWD}/OAICollectionResponseFolder.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIFile.h \
    $${PWD}/OAIFileActionResponse.h \
    $${PWD}/OAIFileStat.h \
    $${PWD}/OAIFileUpdateInput.h \
    $${PWD}/OAIFolder.h \
    $${PWD}/OAIFolderActionResponse.h \
    $${PWD}/OAIFolderInput.h \
    $${PWD}/OAIFolderUpdateInput.h \
    $${PWD}/OAIFolderUpdateTaskLocator.h \
    $${PWD}/OAIImportFromUrlInput.h \
    $${PWD}/OAIImportFromUrlTaskLocator.h \
    $${PWD}/OAINextPage.h \
    $${PWD}/OAIPaging.h \
    $${PWD}/OAIPreviousPage.h \
    $${PWD}/OAISignedUrl.h \
    $${PWD}/OAIStandardError.h \
# APIs
    $${PWD}/OAIFilesApi.h \
    $${PWD}/OAIFoldersApi.h \
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
    $${PWD}/OAICollectionResponseFile.cpp \
    $${PWD}/OAICollectionResponseFolder.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIFile.cpp \
    $${PWD}/OAIFileActionResponse.cpp \
    $${PWD}/OAIFileStat.cpp \
    $${PWD}/OAIFileUpdateInput.cpp \
    $${PWD}/OAIFolder.cpp \
    $${PWD}/OAIFolderActionResponse.cpp \
    $${PWD}/OAIFolderInput.cpp \
    $${PWD}/OAIFolderUpdateInput.cpp \
    $${PWD}/OAIFolderUpdateTaskLocator.cpp \
    $${PWD}/OAIImportFromUrlInput.cpp \
    $${PWD}/OAIImportFromUrlTaskLocator.cpp \
    $${PWD}/OAINextPage.cpp \
    $${PWD}/OAIPaging.cpp \
    $${PWD}/OAIPreviousPage.cpp \
    $${PWD}/OAISignedUrl.cpp \
    $${PWD}/OAIStandardError.cpp \
# APIs
    $${PWD}/OAIFilesApi.cpp \
    $${PWD}/OAIFoldersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
