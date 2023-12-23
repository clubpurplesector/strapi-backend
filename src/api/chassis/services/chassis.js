'use strict';

/**
 * chassis service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::chassis.chassis');
