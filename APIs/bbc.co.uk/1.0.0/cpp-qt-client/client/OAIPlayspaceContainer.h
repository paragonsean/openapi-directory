/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlayspaceContainer.h
 *
 * 
 */

#ifndef OAIPlayspaceContainer_H
#define OAIPlayspaceContainer_H

#include <QJsonObject>

#include "OAIPlayableItem.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPlayableItem;

class OAIPlayspaceContainer : public OAIObject {
public:
    OAIPlayspaceContainer();
    OAIPlayspaceContainer(QString json);
    ~OAIPlayspaceContainer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<OAIPlayableItem> getMembers() const;
    void setMembers(const QList<OAIPlayableItem> &members);
    bool is_members_Set() const;
    bool is_members_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<OAIPlayableItem> m_members;
    bool m_members_isSet;
    bool m_members_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayspaceContainer)

#endif // OAIPlayspaceContainer_H
