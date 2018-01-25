from flask_script import Manager
from exac import app
import exac

manager = Manager(app)


@manager.command
def hello():
    print "hello"


@manager.command
def load_db():
    exac.load_db()
#
#
# @manager.command
# def load_base_coverage():
#     exac.load_base_coverage()

@manager.command
def load_base_coverage_exomes():
    exac.load_base_coverage_exomes()

@manager.command
def load_base_coverage_genomes():
    exac.load_base_coverage_genomes()

@manager.command
def load_exome_variants():
    exac.load_exome_variants()

@manager.command
def load_genome_variants():
    exac.load_genome_variants()

@manager.command
def drop_exome_variants():
    exac.drop_exome_variants()

@manager.command
def drop_genome_variants():
    exac.drop_genome_variants()

@manager.command
def environment_test():
    exac.environment_test()

@manager.command
def reload_variants():
    exac.load_exome_variants()
    exac.load_mnps()
    exac.precalculate_metrics()


@manager.command
def load_gene_models():
    exac.load_gene_models()


@manager.command
def load_cnv_models():
    exac.load_cnv_models()


@manager.command
def load_cnv_genes():
    exac.load_cnv_genes()


@manager.command
def drop_cnv_genes():
    exac.drop_cnv_genes()


@manager.command
def load_dbsnp_file():
    exac.load_dbsnp_file()


@manager.command
def load_constraint_information():
    exac.load_constraint_information()


@manager.command
def load_mnps():
    exac.load_mnps()


@manager.command
def create_cache():
    exac.create_cache()


@manager.command
def precalculate_metrics_exomes():
    exac.precalculate_metrics_exomes()

@manager.command
def precalculate_metrics_genomes():
    exac.precalculate_metrics_genomes()

if __name__ == "__main__":
    manager.run()

