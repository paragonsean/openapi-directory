/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIErrors_ListForGroup_200_response.h
 *
 * 
 */

#ifndef OAIErrors_ListForGroup_200_response_H
#define OAIErrors_ListForGroup_200_response_H

#include <QJsonObject>

#include "OAIErrors_ListForGroup_200_response_errors_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIErrors_ListForGroup_200_response_errors_inner;

class OAIErrors_ListForGroup_200_response : public OAIObject {
public:
    OAIErrors_ListForGroup_200_response();
    OAIErrors_ListForGroup_200_response(QString json);
    ~OAIErrors_ListForGroup_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIErrors_ListForGroup_200_response_errors_inner> getErrors() const;
    void setErrors(const QList<OAIErrors_ListForGroup_200_response_errors_inner> &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIErrors_ListForGroup_200_response_errors_inner> m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIErrors_ListForGroup_200_response)

#endif // OAIErrors_ListForGroup_200_response_H
