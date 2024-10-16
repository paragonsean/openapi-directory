/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRfeItemSimpleVO.h
 *
 * Java type: com.noosh.nooshapi.vo.RfeItemSimpleVO
 */

#ifndef OAIRfeItemSimpleVO_H
#define OAIRfeItemSimpleVO_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRfeItemSimpleVO : public OAIObject {
public:
    OAIRfeItemSimpleVO();
    OAIRfeItemSimpleVO(QString json);
    ~OAIRfeItemSimpleVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getRfeItemId() const;
    void setRfeItemId(const qint64 &rfe_item_id);
    bool is_rfe_item_id_Set() const;
    bool is_rfe_item_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_rfe_item_id;
    bool m_rfe_item_id_isSet;
    bool m_rfe_item_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRfeItemSimpleVO)

#endif // OAIRfeItemSimpleVO_H
