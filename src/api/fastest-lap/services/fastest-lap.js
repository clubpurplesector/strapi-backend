'use strict';

/**
 * fastest-lap service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::fastest-lap.fastest-lap');
