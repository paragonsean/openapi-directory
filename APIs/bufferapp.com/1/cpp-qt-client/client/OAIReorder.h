/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIReorder.h
 *
 * 
 */

#ifndef OAIReorder_H
#define OAIReorder_H

#include <QJsonObject>

#include "OAIReorder_updates_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIReorder_updates_inner;

class OAIReorder : public OAIObject {
public:
    OAIReorder();
    OAIReorder(QString json);
    ~OAIReorder() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    QList<OAIReorder_updates_inner> getUpdates() const;
    void setUpdates(const QList<OAIReorder_updates_inner> &updates);
    bool is_updates_Set() const;
    bool is_updates_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;

    QList<OAIReorder_updates_inner> m_updates;
    bool m_updates_isSet;
    bool m_updates_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReorder)

#endif // OAIReorder_H
