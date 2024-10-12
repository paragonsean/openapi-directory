/**
 * RecoveryServicesBackupClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIJobResourceList.h
 *
 * List of Job resources
 */

#ifndef OAIJobResourceList_H
#define OAIJobResourceList_H

#include <QJsonObject>

#include "OAIJobResource.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIJobResource;

class OAIJobResourceList : public OAIObject {
public:
    OAIJobResourceList();
    OAIJobResourceList(QString json);
    ~OAIJobResourceList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIJobResource> getValue() const;
    void setValue(const QList<OAIJobResource> &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    QString getNextLink() const;
    void setNextLink(const QString &next_link);
    bool is_next_link_Set() const;
    bool is_next_link_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIJobResource> m_value;
    bool m_value_isSet;
    bool m_value_isValid;

    QString m_next_link;
    bool m_next_link_isSet;
    bool m_next_link_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIJobResourceList)

#endif // OAIJobResourceList_H
